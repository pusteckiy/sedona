local sampev = require('samp.events')

function sampev.onShowDialog(id, style, title, btn1, btn2, text)
    print(id)
    print(style)
    print(title)
    print(btn1)
    print(btn2)
    print(text)
end