class Node_tree: 
  def __init__(self, question: str, yes_node: object, no_node: object):
    self.question = question
    self.yes_node = yes_node
    self.no_node = no_node

  def append(self, question: str, yes_node: object, no_node: object):
    self.yes_node.append(question,yes_node,no_node)
    self.no_node.append(question,yes_node,no_node)
    
class Tree:
  def __init__(self,first_question):
    self.first_node = Node_tree(first_question,[])
    self.current_node = self.first_node

  def append_question(self,question,reponses,previous_question):
    self.first_node.append(question,reponses,previous_question)

  def get_question(self):
    return self.current_node.question

  def send_answer(self, reponse):
    for N in self.current_node.next_nodes:
      if N.reponses == reponse:
        self.current_node = N
        break
    return self.current_node.question