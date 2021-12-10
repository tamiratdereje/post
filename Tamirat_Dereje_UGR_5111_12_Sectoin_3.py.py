text = ""
'''
open the attached text and change it to string
'''
''' do not forget to connect ur text file'''
# html_text = open(r"C:\Users\DELL\Desktop\projects\my\real.txt")

html_text = open(r"")
for line in html_text:
    text += line

dictionary = {'<html>': '</html>', '<head>': '</head>', '<title>': '</title>',
     '<body>': '</body>', '<p>': '</p>', '<div>': '</div>',
     '<span>': '</span>', '<a>': '</a>', '<table>': '</table>',
     '<thead>': '</thead>', '<tbody>': '</tbody>', '<tr>': '</tr>',
     '<td>': '</td>', '<script>': '</script>', '<ul>': '</ul>',
     '<li>': '</li>', '<h1>': '</h1>', '<h2>': '</h2>',
     '<strong>': '</strong>', '<h3>': '</h3>', '<h4>': '</h4>',
     '<h5>': '</h5>', '<h6>': '</h6>', '<center>': '</center>'
              }


def checker(string):

    string = string.strip()
    string = string.replace(" ", "_")
    '''
    # just to make the string comfortable for spliting
    '''
    string = string.replace('<', ' <')
    string = string.replace('>', '> ')
    string = string.split()
    '''
    split the string using space and place in the form of element of the list
    '''
    # print(string)
    listOfNewTag = []
    for tag in string:
        '''
        to check the tags weather they contain the tags sign(character)
        '''
        if "_" in tag and tag.startswith('<'):
            '''
            to replace the text inside the the tags
            '''
            tagElemnet = tag.replace(tag[tag.find("_"):], ">")
            listOfNewTag.append(tagElemnet)
        elif tag.startswith('<') and "_" not in tag:
            '''
            append tags in the list
            '''
            listOfNewTag.append(tag)

    print(listOfNewTag, "this is the new tag list")
    listToBeChecked = []
    for i in listOfNewTag:
        if i.startswith('<'):
            '''
            to check weather the tags in list are also
            in the dictionary and append it to new list 
            in order to check weather it is closed or not.
            '''
            if i in dictionary.keys():

                listToBeChecked.append(i)
            else:
                if len(listToBeChecked) == 0:
                    return False
                '''
                if the length of listToBeChecked equals to 0, imply that the tag is not in the library or it is invalid  
                '''
                if dictionary[listToBeChecked[-1]] != i:
                    # to check weather the last tag is closed or not if is not closed make it invalid
                    return False

                else:
                    listToBeChecked.pop()
                    '''
                    to remove the last tag if it is closed 
                    '''

    if len(listToBeChecked) != 0:
        '''
        if still there is tag left closed
        
        '''

        return False
    if len(listToBeChecked) == 0:
        '''
        if all tags are closed 
        '''
        return True


'''
to the call the function 
'''


interpreter = checker(text)
if interpreter:
    print("it is valid")
else:
    print("it is Invalid")
