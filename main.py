import plyj.model as model
import plyj.parser as plyj
import pprint

class RecursionChecker(model.Visitor):
    def __init__(self, needle):
        super(RecursionChecker, self).__init__()
        self.needle = needle
        
    def visit_MethodInvocation(self, t):
        print t.name == self.needle

parser = plyj.Parser()
def check_work(java_file):
    parsed = parser.parse_file(java_file)
    for a_class in parsed.type_declarations:
        for declaration in a_class.body:
            if isinstance(declaration, plyj.MethodDeclaration):
                name = declaration.name
                declaration.accept(RecursionChecker(name))
    
check_work("work/good.java")
