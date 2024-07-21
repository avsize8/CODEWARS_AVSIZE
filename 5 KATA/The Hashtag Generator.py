def generate_hashtag(s):
    if len(s)==0:
        return False
    lst = s.split(" ")
    
    result = "#"
    
    for item in lst:
        result += item.strip().capitalize()
        
    if len(result)>140:
        return False
    
    return result