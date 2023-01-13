import YData as ydata


def test_download_homework():
    """
    Make sure I can download homework files
    """
    
    ydata.download_homework(-1)
    
    # assert...
    

"""
    
github_file_names = ydata.get_github_file_names()






from myPackage import somePython

def test_fahrToKelv():
    '''
    make sure freezing is calculated correctly
    '''
    
    assert somePython.fahrToKelv(32) == 273.15, 'incorrect freezing point!'
    
"""