import os, glob

base = r'C:\Users\TyAAr\OneDrive\Desktop\ARC Affiliates\InnovationsWellness-and-MedSpa'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True)

CSS = """
/* ===== LEAD CAPTURE MODAL ===== */
.lcm-overlay{display:none;position:fixed;inset:0;background:rgba(42,31,26,0.62);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);z-index:99950;align-items:center;justify-content:center;padding:1rem;}
.lcm-overlay.open{display:flex;}
.lcm-box{background:var(--white);max-width:440px;width:100%;padding:2.75rem 2.5rem 2rem;position:relative;box-shadow:0 32px 80px rgba(42,31,26,0.25);}
.lcm-close{position:absolute;top:0.9rem;right:1rem;background:none;border:none;font-size:1.6rem;color:var(--muted);cursor:pointer;line-height:1;padding:0.2rem 0.4rem;transition:color 0.2s;}
.lcm-close:hover{color:var(--ink);}
.lcm-eyebrow{font-size:0.56rem;letter-spacing:0.22em;text-transform:uppercase;color:var(--rose);margin-bottom:0.55rem;}
.lcm-title{font-family:'Playfair Display',serif;font-size:1.65rem;font-weight:400;color:var(--ink);line-height:1.2;margin-bottom:0.6rem;}
.lcm-sub{font-size:0.8rem;color:var(--muted);line-height:1.75;margin-bottom:1.75rem;border-left:2px solid var(--rose);padding-left:0.9rem;}
.lcm-field{margin-bottom:0.9rem;}
.lcm-field label{display:block;font-size:0.55rem;letter-spacing:0.18em;text-transform:uppercase;color:var(--muted);margin-bottom:0.35rem;font-weight:500;}
.lcm-field input{width:100%;border:1px solid var(--line);background:var(--bg);padding:0.72rem 0.9rem;font-family:'DM Sans',sans-serif;font-size:0.88rem;color:var(--ink);outline:none;transition:border-color 0.2s,background 0.2s;}
.lcm-field input:focus{border-color:var(--rose);background:var(--white);}
.lcm-field input.lcm-error{border-color:#c0392b;}
.lcm-submit{width:100%;background:var(--rose);color:#fff;border:none;padding:1rem;font-family:'DM Sans',sans-serif;font-size:0.6rem;font-weight:500;letter-spacing:0.22em;text-transform:uppercase;cursor:pointer;transition:background 0.25s,transform 0.2s;margin-top:0.5rem;}
.lcm-submit:hover:not(:disabled){background:var(--rose2);transform:translateY(-1px);}
.lcm-submit:disabled{opacity:0.65;cursor:not-allowed;transform:none;}
.lcm-skip{text-align:center;margin-top:0.9rem;font-size:0.58rem;color:var(--muted2);}
.lcm-skip a{color:var(--muted2);text-decoration:underline;cursor:pointer;}
.lcm-skip a:hover{color:var(--muted);}
.lcm-divider{display:flex;align-items:center;gap:0.75rem;margin:1.25rem 0 0.35rem;opacity:0.35;}
.lcm-divider span{height:1px;flex:1;background:var(--line);}
.lcm-stars{display:flex;gap:3px;justify-content:center;margin-bottom:0.4rem;}
.lcm-stars svg{width:14px;height:14px;fill:#f5a623;}
.lcm-social-proof{font-size:0.58rem;letter-spacing:0.08em;color:var(--muted2);text-align:center;}
@media(max-width:480px){.lcm-box{padding:2rem 1.35rem 1.5rem;}.lcm-title{font-size:1.35rem;}}
"""

MODAL_HTML = """
<!-- LEAD CAPTURE MODAL -->
<div id="lcm" class="lcm-overlay" role="dialog" aria-modal="true" aria-labelledby="lcm-heading">
  <div class="lcm-box">
    <button class="lcm-close" aria-label="Close" id="lcm-close">&times;</button>
    <div class="lcm-stars" aria-hidden="true">
      <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    </div>
    <div class="lcm-social-proof">5.0 &mdash; Google Reviews &nbsp;&bull;&nbsp; Canton, GA</div>
    <div class="lcm-divider"><span></span></div>
    <div class="lcm-eyebrow">One Quick Step</div>
    <h2 class="lcm-title" id="lcm-heading">Reserve Your Visit</h2>
    <p class="lcm-sub">We&#8217;d love to keep you in the loop on specials and follow up after your visit. Enter your info and we&#8217;ll take you right to booking.</p>
    <form id="lcm-form" novalidate>
      <input type="hidden" name="access_key" value="REPLACE_WITH_WEB3FORMS_KEY">
      <input type="hidden" name="subject" value="New Booking Lead &#8212; Innovations Wellness MedSpa">
      <input type="hidden" name="from_name" value="Innovations Wellness Website">
      <div class="lcm-field">
        <label for="lcm-name">Full Name</label>
        <input type="text" id="lcm-name" name="name" placeholder="Jane Smith" required autocomplete="name">
      </div>
      <div class="lcm-field">
        <label for="lcm-email">Email Address</label>
        <input type="email" id="lcm-email" name="email" placeholder="jane@email.com" required autocomplete="email">
      </div>
      <div class="lcm-field">
        <label for="lcm-phone">Phone Number</label>
        <input type="tel" id="lcm-phone" name="phone" placeholder="(770) 555-0100" required autocomplete="tel">
      </div>
      <button type="submit" class="lcm-submit" id="lcm-btn">Continue to Booking &rarr;</button>
    </form>
    <div class="lcm-skip"><a id="lcm-skip">Skip &mdash; take me straight to booking</a></div>
  </div>
</div>
<script>
(function(){
  var BOOKING='https://web2.myaestheticspro.com/BN/index.cfm?4925808AC514C6FB3E166971F46892EB';
  var ov=document.getElementById('lcm');
  var form=document.getElementById('lcm-form');
  var btn=document.getElementById('lcm-btn');
  function openModal(e){if(e){e.preventDefault();e.stopPropagation();}ov.classList.add('open');document.body.style.overflow='hidden';setTimeout(function(){document.getElementById('lcm-name').focus();},50);}
  function closeModal(){ov.classList.remove('open');document.body.style.overflow='';btn.textContent='Continue to Booking \\u2192';btn.disabled=false;}
  function goBook(){closeModal();window.open(BOOKING,'_blank','noopener,noreferrer');}
  document.querySelectorAll('a[href*="myaestheticspro"]').forEach(function(a){a.addEventListener('click',openModal);});
  document.getElementById('lcm-close').addEventListener('click',closeModal);
  document.getElementById('lcm-skip').addEventListener('click',goBook);
  ov.addEventListener('click',function(e){if(e.target===ov)closeModal();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&ov.classList.contains('open'))closeModal();});
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var fields=[document.getElementById('lcm-name'),document.getElementById('lcm-email'),document.getElementById('lcm-phone')];
    var ok=true;
    fields.forEach(function(f){f.classList.remove('lcm-error');if(!f.value.trim()){f.classList.add('lcm-error');ok=false;}});
    if(!ok)return;
    btn.textContent='Sending\\u2026';btn.disabled=true;
    fetch('https://api.web3forms.com/submit',{method:'POST',body:new FormData(form)})
      .then(function(){goBook();}).catch(function(){goBook();});
  });
})();
</script>
"""

changed = []
skipped = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    if '</style>' not in content or '</body>' not in content:
        skipped.append(os.path.relpath(f, base))
        continue
    if 'lcm-overlay' in content:
        skipped.append(os.path.relpath(f, base) + ' (already has modal)')
        continue
    content = content.replace('</style>', CSS + '</style>', 1)
    content = content.replace('</body>', MODAL_HTML + '\n</body>', 1)
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    changed.append(os.path.relpath(f, base))

print(f'Updated {len(changed)} files:')
for f in changed: print('  ', f)
if skipped:
    print(f'\nSkipped {len(skipped)}:')
    for f in skipped: print('  ', f)
