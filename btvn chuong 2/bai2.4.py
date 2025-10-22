import xml.dom.minidom

def main():
    doc=xml.dom.minidom.parse('bai2.3_sample.xml')
    print(doc.nodeName)
    print(doc.firstChild.tagName)
if __name__=='__main__':
    main()