#!/usr/bin/python3
"""bullshit"""
import sys
import hashlib 

def file_entrance(markdown_file, output_html_name):
    """
    First step in which File is processed in order
    to convert it to HTML format
    @param: markdown_file: file with markdown format to
            be converted to html
    @param: name of the final html converted file
    """
    try:
        open(markdown_file, 'r')
        mark_down_parser(markdown_file, output_html_name)
    except IOError:
        print("Missing {file}".format(file=markdown_file))
        exit(1)

def mark_down_parser(filename, output_html_name):
    """
    bullshit 1
    """
    ul = False
    text = False
    with open(filename, 'r') as f:
        mark_down = f.readlines()
        new_html = ""
        for mark_line in mark_down:
            if mark_line[0] == "#":
                new_html = headings(mark_line, new_html)
                ul = False
            elif mark_line[0] == "-":
                new_html = lists(mark_line, new_html, ul, "-")
                ul = True
            elif mark_line[0] == "*":
                new_html = lists(mark_line, new_html, ul, "*")
                ul = True
            elif mark_line[0] not in ['*', '-']:
                if len(mark_line) > 1:
                    br = True if text else False
                    new_html = text_html(mark_line, new_html, text, br)
                    text = True
                else:
                    text = False
    return create_html(new_html, output_html_name)

def create_html(almost_html, output_html_name):
    """
    bullshit 2
    """
    file = open(output_html_name, "w") 
    file.write(almost_html) 
    file.close()
    return file

def headings(line, new_html):
    """
    bullshit 3
    """
    kind = line.count("#")
    chars = line.split()
    heading = string_cleaner(chars, "#")
    return new_html + add_h_tags(heading, str(kind))

def string_cleaner(string, to_clean):
    """
    bullshit 4
    """
    return [
        m if m != "c" else "" 
        for c in string 
        for m in c if m != to_clean]


def add_h_tags(almost_html, kind):
    """
    bullshit 5
    """
    text = ""
    tags = ["<", "/", "h", kind, ">"]
    for t in tags:
        almost_html.append(t)
    for t in tags[::-1]:
        if t != "/":
            almost_html.insert(0, t)
    almost_html.append("\n")
    return text.join(almost_html)

def lists(line, new_html, ul, symbol):
    """
    bullshit 6
    """
    kind = line.count(symbol)
    chars = line.split()
    prev = None
    if ul and new_html[-6:].strip() in ["<ol>", "</ol>", "<ul>", "</ul>"]:
        prev = "*" if "ol" in new_html[-6:].strip() else "-"
        new_html = remover(new_html)
    ulist = string_cleaner(chars, symbol)
    return new_html + md5_n_c(bold_n_emphasis(add_ul_tags(ulist, ul, symbol, prev)))

def remover(new_html):
    """
    bullshit 7
    """
    remove_cul = new_html.splitlines()
    for i in range(len(remove_cul)):
        remove_cul[i] = remove_cul[i] + "\n"
    remove_cul.pop()
    new_html = "".join(remove_cul)
    return new_html
    
def add_ul_tags(almost_html, ul, symbol, prev):
    """
    bullhshit 8
    """
    text = ""
    if symbol == "-":
        ul_format = ["<ul>", "\n", "<li>",  "</li>", "\n", "</ul>", "\n"]
    else:
        ul_format = ["<ol>", "\n", "<li>",  "</li>", "\n", "</ol>", "\n"]
    if ul and symbol == prev:
        for i in range(2):
            del ul_format[0]
        for c in almost_html[::-1]:
            ul_format.insert(1, c)
    else:
        for c in almost_html[::-1]:
            ul_format.insert(3, c)
    almost_html = ul_format
    return text.join(almost_html)

def text_html(line, new_html, text, br):
    """
    bullshit 9
    """
    chars = line.split()
    chars.insert(0, "\t")
    prev =  None
    if text and new_html[-5:].strip() in ["<p>", "</p>"]:
        prev = '<p>'
    text_format = ["<p>", "\n", "\n", "</p>", "\n"]
    already = 0
    if br:
        if prev:
            chars.append("\n\t<br/>")
            text_format = text_format[:3]
            expand = range(len(chars))
            chars = add_add_spaces(chars)
            for c in chars[::-1]:
                text_format.insert(2, c)
                already = 1
        else:
            chars.append("\n</p>")
            chars = add_add_spaces(chars)
            return md5_n_c(bold_n_emphasis(new_html + "".join(chars)))
    if not already:
        chars = add_add_spaces(chars)
        for c in chars[::-1]:
            text_format.insert(2, c)
    html = md5_n_c(bold_n_emphasis("".join(text_format)))
    return new_html + html

def add_add_spaces(chars):
    """
    bullshit 10
    """
    add = []
    expand = 0
    for i in range(len(chars)):
        if i % 2 == 0:
            add.append(i + expand)
            expand += 1

    add.append(add[-1] - 1)
    for i in add:
        chars.insert(i, " ")
    return chars

def bold_n_emphasis(html_to_new):
    """
     bullshit 12
    """
    em = False
    index = html_to_new.find("**", 0, len(html_to_new))
    index_2 = html_to_new.find("**", index + 1, len(html_to_new))
    if index == -1:
        em = True
        index = html_to_new.find("__", 0, len(html_to_new))
        index_2 = html_to_new.find("__", index + 1, len(html_to_new))
    if index != -1 and index_2 != -1:
        if not em:
            transform = html_to_new[index + 2:index_2]
            transform = "<b>" + transform + "</b>"
        else:
            transform = html_to_new[index + 2:index_2]
            transform = "<em>" + transform + "</em>"
        html_to_new = html_to_new[:index] + transform + html_to_new[index_2 + 2:]
    return html_to_new

def md5_n_c(html_to_new):
    """
    bullshit 13
    """
    c = False
    index = html_to_new.find("[[", 0, len(html_to_new))
    index_2 = html_to_new.find("]]", index + 1, len(html_to_new))
    if index == -1:
        c = True
        index = html_to_new.find("((", 0, len(html_to_new))
        index_2 = html_to_new.find("))", index + 1, len(html_to_new))
    if index != -1 and index_2 != -1:
        if not c:
            transform = html_to_new[index + 2:index_2]
            transform = hashlib.md5(transform.encode()).hexdigest()
        else:
            transform = html_to_new[index + 2: index_2]
            transform = transform.replace("c", "")
            transform = transform.replace("C", "")
        html_to_new = html_to_new[:index] + transform + html_to_new[index_2 + 2:]
    return html_to_new
            
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    file_entrance(sys.argv[1], sys.argv[2])
