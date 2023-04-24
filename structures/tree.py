class tree:
  def __init__(self,first_question):
    self.first_node = node(first_question,[])
    self.current_node = self.first_node

  def append_question(self,question,reponses,previous_question):
    self.first_node.append(question,reponses,previous_question)

  def delete_question(self,question):
    if self.first_node.question == question:
      self.first_node = None
    else:
      self.first_node.delete(question)

  def get_question(self):
    return self.current_node.question

  def send_answer(self, reponse):
    for N in self.current_node.next_nodes:
      if N.reponses == reponse:
        self.current_node = N
        break
    return self.current_node.question