import urllib.request
import re

url = 'https://ajaykumar-me.vercel.app'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as res:
    html = res.read().decode('utf-8')
    print('HTML Status:', res.status)

m = re.search(r'src="(/assets/[^"]+\.js)"', html)
if m:
    js_url = url + m.group(1)
    print('Testing JS Bundle:', js_url)
    with urllib.request.urlopen(urllib.request.Request(js_url, headers={'User-Agent': 'Mozilla/5.0'})) as js_res:
        js = js_res.read().decode('utf-8', errors='ignore')
        print('SmartCart Topaz link present:', 'smart-cart-topaz-ten' in js)
        print('SkillForge Tau-Vert link present:', 'skillforge-tau-vert' in js)
        print('EduNova link present:', 'ajay-erp-management' in js)
        print('FormSubmit.co API present:', 'formsubmit.co' in js)
        print('General Full Stack Developer present:', 'Full Stack Developer' in js)
        print('GitHub link present:', 'Ajaykumar-110' in js)

# Also test PDF resume
resume_url = 'https://ajaykumar-me.vercel.app/Ajaykumar_Resume.pdf'
try:
    with urllib.request.urlopen(urllib.request.Request(resume_url, headers={'User-Agent': 'Mozilla/5.0'})) as pdf_res:
        print('Resume PDF Status:', pdf_res.status, 'Size:', len(pdf_res.read()), 'bytes')
except Exception as e:
    print('Resume PDF Error:', e)
