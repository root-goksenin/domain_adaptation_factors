from src.utils import normalize     


def return_query_type(query: str) -> str: 
    first_word = query.split(" ")[0].lower().strip()
    yes_and_no = ["is", "was", "are", "were", "do", "does", "did", "have", "has", "had", "should", "can", "would", "could", "am", "shall"]
    if first_word in ["what", "what\'s"]:
        return "What"
    elif first_word in ["how", "how\'s"]:
        return "How"
    elif first_word in ["why", "why\'s"]:
        return "Why"
    elif first_word in ["when", "when\'s"]:
        return "When"
    elif first_word in ["where", "where\'s"]:
        return "Where"
    elif first_word in ["which", "which\'s"]:
        return "Which"
    elif first_word in ["who", "who\'s"]:
        return "Who"
    elif first_word in yes_and_no:
        return "Y/N"
    else:
        return "Declerative"    
    
def check_query_type_distribution(queries):
    c = {"What": 0,
         "How" : 0, 
         "Why" : 0,
         "When" : 0,   
         "Where": 0,
         "Which": 0,
         "Who" : 0,
         "Y/N" : 0,
         "Declerative": 0}
    for query in queries.values():
        c[return_query_type(query)] += 1
    return normalize(c)