#import eval_score_matrix_foldout

try:
    from cpp.evaluate_foldout import eval_score_matrix_foldout
    print("eval_score_matrix_foldout with cpp")
except:
    from python.evaluate_foldout import eval_score_matrix_foldout
    print("eval_score_matrix_foldout with python")
    
