import anki

lang = anki.lang.current_lang


def getTr(s: str) -> str:
    if lang != 'zh-CN':
        return s
    else:
        if s == 'Copy note ID':
            return '复制笔记ID'
        elif s == 'Copy note link':
            return '复制笔记链接'
        elif s == 'Open note in new window':
            return '在新窗口中打开笔记'
        elif s == 'Show/Hide Link Page':
            return '显示/隐藏链接页面'
        elif s == 'The corresponding note does not exist':
            return '对应笔记不存在'
        elif s == 'Please add the current note first':
            return '请先添加当前笔记'
        else:
            return s