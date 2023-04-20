class node_tree: 
  def __init__(self, question, reponses):
    self.question = question
    self.reponses = reponses
    self.next_nodes = []

  def append(self, question,reponses,previous_question):
    if previous_question == self.question:
      self.next_nodes.append(node(question,reponses))
    else:
      for N in self.next_nodes:
        N.append(question,reponses,previous_question)

  def delete(self,question):
    for N in self.next_nodes:
        if N.question == question:
            del N # delete the node
    else:
        N.delete(question)