class LinkedList:
  def __init__(self, data):
    self.first_node = Node(data) # On crée le premier noeud
    self.last_node = self.first_node

  def append(self,data): # Ajoute une data à la fin de la liste
    self.last_node.next_node = Node(data) # On crée un nouveau noeud et on le met comme suivant du dernier noeud
    self.last_node = self.last_node.next_node # On met à jour le dernier noeud

  def size(self): # Renvoie la taille de la liste
    count = 0
    current_node = self.first_node
    while current_node != None:
      count += 1
      current_node = current_node.next_node
    return count

  def insert(self, indice, data): #insert une data à un indice précis
    current_node = self.first_node # On sauvegarde le premier noeud
    
    while indice > 0: # On se déplace jusqu'à l'indice précisé
      current_node = current_node.next_node # On avance d'un noeud
      indice -= 1 # On décrémente l'indice
    
    current_node.next_node, current_node.next_node.next_node = Node(data), current_node.next_node # On crée un nouveau noeud et on le met comme suivant du noeud courant