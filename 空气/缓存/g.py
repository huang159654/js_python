import execjs


texr='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'
json=execjs.compile(open('dome.js','r',encoding='utf_8').read()).call('getValue',texr)
print(json)
