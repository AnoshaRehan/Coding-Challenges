from bs4 import BeautifulSoup

def dom_tree(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_tables = soup.select("table")
    # print(all_tables)
    rows = []
    for table in all_tables:
        row = table.select("td")
        rows.append(len(row))
    return max(rows)
    
print(dom_tree("<div> <p>First table</p> <table> <tr> <td>First</td> <td>row</td></tr><tr><td>and</td><td>second</td><td>row</td></tr><tr><td>and</td><td>the</td><td>third</td><td>one</td></tr></table></div><p>Second table</p><table><tr><td>t</td><td>t1</td></tr><tr><td>td3</td><td>td4</td></tr></table>"))  
