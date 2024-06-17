from text_formatting_app import join_text, capitalize_text, titlecase_text, uppercase_text

def test_join_text():
    assert join_text('he', 'llo') == 'hello'
    assert join_text('pi', 'zza') == 'pizza'

def test_capitalize_text():
    assert capitalize_text('have a NICE day') == 'Have a nice day'
    assert capitalize_text('gOod MoRnING') == 'Good morning'

def test_titlecase_text():
    assert titlecase_text('have a NICE day') == 'Have A Nice Day'
    assert titlecase_text('gOod MoRnING') == 'Good Morning'

def test_uppercase_text():
    assert titlecase_text('have a NICE day') == 'HAVE A NICE DAY'
    assert titlecase_text('gOod MoRnING') == 'GOOD MORNING'