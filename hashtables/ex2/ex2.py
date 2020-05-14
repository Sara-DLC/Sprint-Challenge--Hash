#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # start ticket dict and route list
    ticket = {}
    route = []
# for every ticket item set ticket source as the ticket destination
    for i in tickets:
        ticket[i.source] = i.destination

    cur = ticket['NONE']
# while there are no tickets append the current ticket to the route and make current
    while cur != 'NONE':
        route.append(cur)
        cur = ticket[cur]

    route.append(cur)

    return route
