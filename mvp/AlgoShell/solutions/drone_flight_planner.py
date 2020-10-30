def calc_drone_min_energy(route):
  diff_list= []
  
  for timestep in range(len(route)-1):
    prev_waypoint = route[timestep]
    curr_waypoint = route[timestep+1]
    diff_list.append(get_alt(prev_waypoint)-get_alt(curr_waypoint))
    
  min_value = float('inf')
  fuel = 0
  for diff in diff_list:
    fuel += diff
    min_value = min(fuel, min_value)
    
  return max(-1*min_value, 0)


def get_alt(route):
  '''
  Get altitude of given waypoint.
  '''
  return route[2]