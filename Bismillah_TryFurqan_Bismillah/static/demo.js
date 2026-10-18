// Bismillah ir-Rahman ir-Rahim
// 
// Al-Asma ul-Husna -- The 99 Beautiful Names of Allah
//   Allah -- The God
//   Ar-Rahman -- The Most Merciful
//   Ar-Rahim -- The Most Compassionate
//   Al-Malik -- The King
//   Al-Quddus -- The Most Holy
//   As-Salam -- The Source of Peace
//   Al-Mu'min -- The Guardian of Faith
//   Al-Muhaymin -- The Protector
//   Al-Aziz -- The Almighty
//   Al-Jabbar -- The Compeller
//   Al-Mutakabbir -- The Supreme
//   Al-Khaliq -- The Creator
//   Al-Bari -- The Evolver
//   Al-Musawwir -- The Fashioner
//   Al-Ghaffar -- The Forgiver
//   Al-Qahhar -- The Subduer
//   Al-Wahhab -- The Bestower
//   Ar-Razzaq -- The Provider
//   Al-Fattah -- The Opener
//   Al-Alim -- The All-Knowing
//   Al-Qabid -- The Restrainer
//   Al-Basit -- The Expander
//   Al-Khafid -- The Abaser
//   Ar-Rafi -- The Exalter
//   Al-Mu'izz -- The Bestower of Honor
//   Al-Mudhill -- The Humiliator
//   As-Sami -- The All-Hearing
//   Al-Basir -- The All-Seeing
//   Al-Hakam -- The Judge
//   Al-Adl -- The Just
//   Al-Latif -- The Subtle One
//   Al-Khabir -- The All-Aware
//   Al-Halim -- The Forbearing
//   Al-Azim -- The Magnificent
//   Al-Ghafur -- The All-Forgiving
//   Ash-Shakur -- The Appreciative
//   Al-Ali -- The Most High
//   Al-Kabir -- The Most Great
//   Al-Hafiz -- The Preserver
//   Al-Muqit -- The Sustainer
//   Al-Hasib -- The Reckoner
//   Al-Jalil -- The Majestic
//   Al-Karim -- The Generous
//   Ar-Raqib -- The Watchful
//   Al-Mujib -- The Responsive
//   Al-Wasi -- The All-Encompassing
//   Al-Hakim -- The Perfectly Wise
//   Al-Wadud -- The Loving One
//   Al-Majid -- The Most Glorious
//   Al-Ba'ith -- The Resurrector
//   Ash-Shahid -- The Witness
//   Al-Haqq -- The Truth
//   Al-Wakil -- The Trustee
//   Al-Qawiyy -- The Most Strong
//   Al-Matin -- The Firm One
//   Al-Waliyy -- The Protector
//   Al-Hamid -- The Praiseworthy
//   Al-Muhsi -- The Accounter
//   Al-Mubdi -- The Originator
//   Al-Mu'id -- The Restorer
//   Al-Muhyi -- The Giver of Life
//   Al-Mumit -- The Creator of Death
//   Al-Hayy -- The Ever Living
//   Al-Qayyum -- The Self-Subsisting
//   Al-Wajid -- The Finder
//   Al-Majid -- The Noble
//   Al-Wahid -- The Unique
//   Al-Ahad -- The One
//   As-Samad -- The Eternal
//   Al-Qadir -- The Able
//   Al-Muqtadir -- The Powerful
//   Al-Muqaddim -- The Expediter
//   Al-Mu'akhkhir -- The Delayer
//   Al-Awwal -- The First
//   Al-Akhir -- The Last
//   Az-Zahir -- The Manifest
//   Al-Batin -- The Hidden
//   Al-Wali -- The Governor
//   Al-Muta'ali -- The Most Exalted
//   Al-Barr -- The Source of Goodness
//   At-Tawwab -- The Acceptor of Repentance
//   Al-Muntaqim -- The Avenger
//   Al-Afuww -- The Pardoner
//   Ar-Ra'uf -- The Most Kind
//   Malik-ul-Mulk -- Owner of Sovereignty
//   Dhul-Jalali wal-Ikram -- Lord of Majesty and Generosity
//   Al-Muqsit -- The Equitable
//   Al-Jami -- The Gatherer
//   Al-Ghaniyy -- The Self-Sufficient
//   Al-Mughni -- The Enricher
//   Al-Mani -- The Preventer
//   Ad-Darr -- The Distresser
//   An-Nafi -- The Propitious
//   An-Nur -- The Light
//   Al-Hadi -- The Guide
//   Al-Badi -- The Originator
//   Al-Baqi -- The Everlasting
//   Al-Warith -- The Inheritor
//   Ar-Rashid -- The Guide to the Right Path
//   As-Sabur -- The Patient
// 
/* tryfurqan demo: paste a .furqan module, see the verdict.
 *
 * Wires the textarea and exhibit buttons to POST /demo/check, then
 * renders the JSON envelope into a verdict panel.
 */
(function () {
  'use strict';

  var $ = function (sel) { return document.querySelector(sel); };
  var sourceEl = $('#source');
  var metaEl = $('#source-meta');
  var checkBtn = $('#check-btn');
  var outputEl = $('#output');

  var MAX_BYTES = 64 * 1024;

  function byteLength(str) {
    return new Blob([str]).size;
  }

  function updateMeta() {
    var n = byteLength(sourceEl.value);
    metaEl.textContent = n.toLocaleString() + ' bytes \u00b7 64 KiB cap';
    if (n > MAX_BYTES) {
      metaEl.style.color = '#B85742';
    } else {
      metaEl.style.color = '';
    }
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  function renderPanel(result) {
    var verdict = result.verdict || 'error';
    var label = result.verdict_label || 'INTERNAL ERROR';

    var heading = '';
    var body = '';

    if (verdict === 'pass') {
      heading = 'The module is structurally honest.';
      body = 'All nine checkers ran. Zero marads, zero advisories. The signature does not promise more than the body delivers.';
    } else if (verdict === 'advisory') {
      heading = 'The module passes, with notes.';
      body = 'No structural violations. The compiler flagged informational findings worth reading; see the output below for the checker name and message.';
    } else if (verdict === 'marad') {
      heading = 'At least one structural violation.';
      body = 'The signature lies on at least one path, or the structure violates a checker invariant. Each marad below names the checker, the diagnosis, and the minimal fix.';
    } else if (verdict === 'parse_error') {
      heading = 'The source could not be parsed.';
      body = 'A tokenize or parse error fired before any checker ran. Diagnostics include the line and column of the failure.';
    } else {
      heading = 'The check did not complete.';
      body = result.error ? String(result.error) : 'See the output panel for details.';
    }

    var output = '';
    if (result.stderr && result.stderr.trim().length) {
      output += result.stderr.trim();
    }
    if (result.stdout && result.stdout.trim().length) {
      if (output.length) output += '\n\n';
      output += result.stdout.trim();
    }
    if (!output.length && result.error) {
      output = String(result.error);
    }

    var elapsed = (result.elapsed_ms != null) ? (result.elapsed_ms + ' ms') : 'n/a';
    var exitCode = (result.exit_code != null) ? result.exit_code : 'n/a';
    var version = result.furqan_version || 'unknown';

    outputEl.innerHTML =
      '<div class="panel ' + verdict + '">' +
        '<div class="verdict-badge verdict-' + verdict + '">' + escapeHtml(label) + '</div>' +
        '<p><strong>' + escapeHtml(heading) + '</strong></p>' +
        '<p style="margin-top:0.4rem;">' + escapeHtml(body) + '</p>' +
        (output ? '<pre class="check-output">' + escapeHtml(output) + '</pre>' : '') +
        '<div class="meta-strip">' +
          '<span><strong>Exit</strong> ' + escapeHtml(exitCode) + '</span>' +
          '<span><strong>Elapsed</strong> ' + escapeHtml(elapsed) + '</span>' +
          '<span><strong>Furqan</strong> ' + escapeHtml(version) + '</span>' +
        '</div>' +
      '</div>';

    outputEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function setBusy(busy) {
    checkBtn.disabled = busy;
    checkBtn.textContent = busy ? 'Checking\u2026' : 'Run check';
  }

  function runCheck() {
    var source = sourceEl.value;
    if (!source || !source.trim().length) {
      outputEl.innerHTML =
        '<div class="panel error">' +
          '<div class="verdict-badge verdict-error">EMPTY</div>' +
          '<p><strong>Nothing to check.</strong></p>' +
          '<p style="margin-top:0.4rem;">Paste a .furqan module or pick an exhibit, then run again.</p>' +
        '</div>';
      return;
    }
    if (byteLength(source) > MAX_BYTES) {
      outputEl.innerHTML =
        '<div class="panel error">' +
          '<div class="verdict-badge verdict-error">INPUT TOO LARGE</div>' +
          '<p><strong>Source exceeds the 64 KiB cap.</strong></p>' +
          '<p style="margin-top:0.4rem;">Trim the input and run again.</p>' +
        '</div>';
      return;
    }

    setBusy(true);
    fetch('/demo/check', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ source: source })
    })
      .then(function (r) {
        if (!r.ok) {
          return r.text().then(function (t) {
            throw new Error('HTTP ' + r.status + ': ' + t);
          });
        }
        return r.json();
      })
      .then(renderPanel)
      .catch(function (err) {
        outputEl.innerHTML =
          '<div class="panel error">' +
            '<div class="verdict-badge verdict-error">REQUEST FAILED</div>' +
            '<p><strong>The check request did not complete.</strong></p>' +
            '<p style="margin-top:0.4rem;">' + escapeHtml(err.message || String(err)) + '</p>' +
          '</div>';
      })
      .finally(function () {
        setBusy(false);
      });
  }

  function loadFixture(name) {
    fetch('/demo/fixtures/' + encodeURIComponent(name))
      .then(function (r) {
        if (!r.ok) throw new Error('fixture not found: ' + name);
        return r.text();
      })
      .then(function (text) {
        sourceEl.value = text;
        updateMeta();
        sourceEl.scrollTop = 0;
        runCheck();
      })
      .catch(function (err) {
        outputEl.innerHTML =
          '<div class="panel error">' +
            '<div class="verdict-badge verdict-error">FIXTURE FAILED</div>' +
            '<p><strong>Could not load the exhibit.</strong></p>' +
            '<p style="margin-top:0.4rem;">' + escapeHtml(err.message || String(err)) + '</p>' +
          '</div>';
      });
  }

  // Wire up
  sourceEl.addEventListener('input', updateMeta);
  checkBtn.addEventListener('click', runCheck);
  document.querySelectorAll('.exhibit').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var name = btn.getAttribute('data-fixture');
      if (name) loadFixture(name);
    });
  });

  // Cmd/Ctrl + Enter shortcut to run the check from the textarea.
  sourceEl.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') {
      e.preventDefault();
      runCheck();
    }
  });

  updateMeta();
})();

// Bismillah ir-Rahman ir-Rahim