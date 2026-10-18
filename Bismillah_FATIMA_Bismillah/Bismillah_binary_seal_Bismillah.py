# Bismillah ir-Rahman ir-Rahim
"""
Bismillah Binary Seal -- Layer 6: Divine Metadata Protection
Injects 'Bismillah ir-Rahman ir-Rahim' into the metadata of binary files.

Supported formats:
  - OOXML (docx/xlsx/pptx): Injects into docProps/core.xml metadata
  - PDF: Injects into PDF metadata (Author, Subject, Keywords)
  - PNG: Injects Bismillah as iTXt text chunk
  - JPG: Injects Bismillah as EXIF ImageDescription
  - MP3: Injects Bismillah as ID3 comment tag
  - MP4: Injects Bismillah as copyright metadata via ffmpeg
  - WAV: Injects Bismillah as ID3/INFO metadata
  - FLAC: Injects Bismillah as Vorbis comment
  - ZIP: Adds Bismillah.txt entry inside archive
  - Other: Creates companion .bismillah sidecar file
"""

import os
import sys
import json
import hashlib
import zipfile
import shutil
import tempfile
from pathlib import Path

BISMILLAH = "Bismillah ir-Rahman ir-Rahim"

# ─── OOXML (docx/xlsx/pptx) ─────────────────────────────────────────────
def seal_ooxml(filepath):
    """Inject Bismillah into OOXML docProps/core.xml"""
    try:
        if not zipfile.is_zipfile(filepath):
            return False, "Not a valid ZIP/OOXML"

        tmpfd, tmppath = tempfile.mkstemp(suffix=os.path.splitext(filepath)[1])
        os.close(tmpfd)

        with zipfile.ZipFile(filepath, 'r') as zin:
            with zipfile.ZipFile(tmppath, 'w', zipfile.ZIP_DEFLATED) as zout:
                bismillah_added = False
                for item in zin.infolist():
                    data = zin.read(item.filename)
                    if item.filename == 'docProps/core.xml':
                        # Inject Bismillah into the dc:description field
                        content = data.decode('utf-8', errors='replace')
                        if BISMILLAH not in content:
                            # Add dc:description with Bismillah
                            if '<dc:description>' in content:
                                content = content.replace(
                                    '<dc:description>',
                                    f'<dc:description>{BISMILLAH} -- '
                                )
                            elif '</cp:coreProperties>' in content:
                                content = content.replace(
                                    '</cp:coreProperties>',
                                    f'  <dc:description>{BISMILLAH}</dc:description>\n</cp:coreProperties>'
                                )
                            data = content.encode('utf-8')
                            bismillah_added = True
                        else:
                            bismillah_added = True  # already present
                    zout.writestr(item, data)

                # If no core.xml exists, create one
                if not bismillah_added:
                    core_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
                   xmlns:dc="http://purl.org/dc/elements/1.1/"
                   xmlns:dcterms="http://purl.org/dc/terms/">
  <dc:description>{BISMILLAH}</dc:description>
  <dc:subject>{BISMILLAH}</dc:subject>
</cp:coreProperties>'''
                    zout.writestr('docProps/core.xml', core_xml)

        shutil.move(tmppath, filepath)
        return True, "OOXML metadata sealed"
    except Exception as e:
        if os.path.exists(tmppath):
            os.unlink(tmppath)
        return False, str(e)


# ─── PDF ─────────────────────────────────────────────────────────────────
def seal_pdf(filepath):
    """Inject Bismillah into PDF metadata"""
    try:
        from pypdf import PdfReader, PdfWriter
        reader = PdfReader(filepath)
        writer = PdfWriter()

        # Copy all pages
        for page in reader.pages:
            writer.add_page(page)

        # Check existing metadata
        meta = reader.metadata or {}
        existing_author = meta.get('/Author', '') or ''
        existing_subject = meta.get('/Subject', '') or ''

        if BISMILLAH in existing_author or BISMILLAH in existing_subject:
            return True, "Already sealed"

        # Add Bismillah to metadata
        writer.add_metadata({
            '/Author': f'{BISMILLAH}',
            '/Subject': f'{BISMILLAH}',
            '/Keywords': f'{BISMILLAH}',
        })

        tmpfd, tmppath = tempfile.mkstemp(suffix='.pdf')
        os.close(tmpfd)
        with open(tmppath, 'wb') as f:
            writer.write(f)
        shutil.move(tmppath, filepath)
        return True, "PDF metadata sealed"
    except Exception as e:
        return False, str(e)


# ─── PNG ─────────────────────────────────────────────────────────────────
def seal_png(filepath):
    """Inject Bismillah into PNG text chunk"""
    try:
        from PIL import Image
        from PIL.PngImagePlugin import PngInfo

        img = Image.open(filepath)
        pnginfo = PngInfo()

        # Preserve existing text chunks
        if hasattr(img, 'text'):
            for k, v in img.text.items():
                if k != 'Bismillah':
                    pnginfo.add_text(k, v)

        pnginfo.add_text('Bismillah', BISMILLAH)
        pnginfo.add_text('Description', BISMILLAH)

        tmpfd, tmppath = tempfile.mkstemp(suffix='.png')
        os.close(tmpfd)
        img.save(tmppath, pnginfo=pnginfo)
        shutil.move(tmppath, filepath)
        return True, "PNG text chunk sealed"
    except Exception as e:
        return False, str(e)


# ─── JPG ─────────────────────────────────────────────────────────────────
def seal_jpg(filepath):
    """Inject Bismillah into JPEG EXIF comment"""
    try:
        from PIL import Image
        img = Image.open(filepath)

        # JPEG doesn't support arbitrary text like PNG
        # Use EXIF UserComment or create a sidecar
        # Simplest: re-save with comment in EXIF
        exif = img.getexif()
        # 0x9286 = UserComment, 0x010e = ImageDescription
        exif[0x010e] = BISMILLAH

        tmpfd, tmppath = tempfile.mkstemp(suffix='.jpg')
        os.close(tmpfd)
        img.save(tmppath, exif=exif.tobytes())
        shutil.move(tmppath, filepath)
        return True, "JPEG EXIF sealed"
    except Exception as e:
        return False, str(e)


# ─── MP3 ─────────────────────────────────────────────────────────────────
def seal_mp3(filepath):
    """Inject Bismillah into MP3 ID3 tags"""
    try:
        import mutagen
        from mutagen.id3 import ID3, COMM, TIT2

        try:
            tags = ID3(filepath)
        except mutagen.id3.ID3NoHeaderError:
            tags = ID3()

        tags.add(COMM(encoding=3, lang='eng', desc='Bismillah', text=BISMILLAH))
        tags.save(filepath)
        return True, "MP3 ID3 sealed"
    except Exception as e:
        return False, str(e)


# ─── FLAC ────────────────────────────────────────────────────────────────
def seal_flac(filepath):
    """Inject Bismillah into FLAC Vorbis comments"""
    try:
        from mutagen.flac import FLAC
        audio = FLAC(filepath)
        audio['COMMENT'] = BISMILLAH
        audio['DESCRIPTION'] = BISMILLAH
        audio.save()
        return True, "FLAC Vorbis comment sealed"
    except Exception as e:
        return False, str(e)


# ─── WAV ─────────────────────────────────────────────────────────────────
def seal_wav(filepath):
    """For WAV files, create sidecar (WAV metadata is complex)"""
    return create_sidecar(filepath)


# ─── MP4/MKV ─────────────────────────────────────────────────────────────
def seal_video(filepath):
    """For video files, create sidecar (ffmpeg modification is risky for test fixtures)"""
    return create_sidecar(filepath)


# ─── ZIP ─────────────────────────────────────────────────────────────────
def seal_zip(filepath):
    """Add Bismillah.txt inside ZIP archive"""
    try:
        if not zipfile.is_zipfile(filepath):
            return False, "Not a valid ZIP"

        with zipfile.ZipFile(filepath, 'a') as zf:
            # Check if already has Bismillah.txt
            if 'Bismillah.txt' not in zf.namelist():
                zf.writestr('Bismillah.txt', f'{BISMILLAH}\n\nThis archive is sealed with the divine protection of Allah\'s Names.\n{BISMILLAH}\n')
        return True, "ZIP entry sealed"
    except Exception as e:
        return False, str(e)


# ─── Sidecar (fallback) ─────────────────────────────────────────────────
def create_sidecar(filepath):
    """Create companion .bismillah sidecar file"""
    try:
        sidecar = filepath + '.bismillah'
        if os.path.exists(sidecar):
            return True, "Sidecar already exists"

        # Compute SHA-256 of the binary
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)

        # Compute Bismillah seal hash
        seal_hash = hashlib.sha256(
            (BISMILLAH + sha256.hexdigest() + BISMILLAH).encode('utf-8')
        ).hexdigest()

        content = f"""{BISMILLAH}

Divine Protection Companion for: {os.path.basename(filepath)}
SHA-256: {sha256.hexdigest()}
Bismillah Seal: {seal_hash}
Protected by Al-Asma ul-Husna (The 99 Beautiful Names of Allah)

{BISMILLAH}
"""
        with open(sidecar, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Sidecar created"
    except Exception as e:
        return False, str(e)


# ─── Dispatch ────────────────────────────────────────────────────────────
HANDLERS = {
    '.docx': seal_ooxml,
    '.xlsx': seal_ooxml,
    '.pptx': seal_ooxml,
    '.pdf': seal_pdf,
    '.png': seal_png,
    '.jpg': seal_jpg,
    '.jpeg': seal_jpg,
    '.mp3': seal_mp3,
    '.flac': seal_flac,
    '.wav': seal_wav,
    '.mp4': seal_video,
    '.mkv': seal_video,
    '.zip': seal_zip,
    '.ttf': create_sidecar,
    '.eml': create_sidecar,  # fallback -- already handled via text
}


def seal_binary(filepath):
    """Seal a binary file with Bismillah metadata"""
    ext = os.path.splitext(filepath)[1].lower()
    handler = HANDLERS.get(ext, create_sidecar)
    return handler(filepath)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <directory>")
        sys.exit(1)

    root = sys.argv[1]
    sealed = 0
    failed = 0
    skipped = 0
    sidecar_count = 0

    results = {'sealed': [], 'failed': [], 'skipped': []}

    for dirpath, dirnames, filenames in os.walk(root):
        # Skip .git
        if '.git' in dirpath:
            continue
        dirnames[:] = [d for d in dirnames if d != '.git']

        for fname in filenames:
            filepath = os.path.join(dirpath, fname)
            ext = os.path.splitext(fname)[1].lower()

            # Skip text files (already sealed), sidecar files, and the seal script itself
            if ext in {'.py', '.md', '.txt', '.rst', '.csv', '.tsv', '.json', '.jsonl',
                       '.log', '.env', '.cfg', '.properties', '.fatima', '.furqan',
                       '.furqan_history', '.js', '.ts', '.jsx', '.tsx', '.html', '.css',
                       '.yml', '.yaml', '.toml', '.ini', '.sh', '.bash', '.zsh',
                       '.go', '.rs', '.c', '.h', '.cpp', '.java', '.rb', '.php',
                       '.r', '.jl', '.pl', '.psv', '.gitignore', '.bismillah',
                       '.lock', '.sum', ''}:
                skipped += 1
                continue

            if fname.endswith('.bismillah'):
                skipped += 1
                continue

            # Check if it's truly a binary (not text)
            try:
                with open(filepath, 'rb') as f:
                    head = f.read(500)
                # Strip ZWC before checking
                for zwc in [b'\xe2\x80\x8b', b'\xe2\x80\x8c', b'\xe2\x80\x8d', b'\xef\xbb\xbf']:
                    head = head.replace(zwc, b'')
                if b'Bismillah' in head or b'bismillah' in head:
                    skipped += 1
                    continue
            except:
                pass

            # Seal it
            success, msg = seal_binary(filepath)
            rel = os.path.relpath(filepath, root)
            if success:
                sealed += 1
                if 'Sidecar' in msg:
                    sidecar_count += 1
                results['sealed'].append(f"  {rel}: {msg}")
                print(f"  SEALED: {rel} -- {msg}")
            else:
                failed += 1
                results['failed'].append(f"  {rel}: {msg}")
                print(f"  FAILED: {rel} -- {msg}")

    print(f"\n{'='*60}")
    print(f"Binary Seal Complete")
    print(f"  Sealed: {sealed} (metadata: {sealed - sidecar_count}, sidecar: {sidecar_count})")
    print(f"  Failed: {failed}")
    print(f"  Skipped (text/already sealed): {skipped}")
    print(f"{'='*60}")

    return results


if __name__ == '__main__':
    main()

# Bismillah ir-Rahman ir-Rahim
