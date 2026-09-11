import urllib.request

url = 'https://ajaykumar-me.vercel.app'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as res:
    data = res.read().decode('utf-8', errors='ignore')

print('Total Length:', len(data))
print('SmartCart:', 'smart-cart-topaz-ten' in data)
print('SkillForge:', 'skillforge-tau-vert' in data)
print('EduNova:', 'ajay-erp-management' in data)
print('FormSubmit:', 'formsubmit.co' in data)
print('Full Stack Developer:', 'Full Stack Developer' in data)
print('GitHub:', 'Ajaykumar-110' in data)
print('Resume PDF link:', 'Ajaykumar_Resume.pdf' in data)
