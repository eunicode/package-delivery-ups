def calculate_shortest_distance(truck_distance_list, truck_number, current_location):

    # Sorting algo helper function
    def manage_queue(organized_list, organized_list_index, index):
        organized_list.append(index)
        organized_list_index.append(index[1])
        pop_value = truck_distance_list.index(index)
        truck_distance_list.pop(pop_value)
        nonlocal current_location
        current_location = new_location

    # section 1
    if len(truck_distance_list) == 0:  # section 2
        return truck_distance_list

    else:  #
        # try:
        # lowest_value = 50.0
        # closest_dist = 50.0
        closest_dist = 14.1  # maximum distance in distances table
        new_location = 0

        # Find closest location to current location
        for index in truck_distance_list:
            if check_current_distance(current_location, int(index[1])) <= closest_dist:
                closest_dist = check_current_distance(
                    current_location, int(index[1])
                )  # section 3
                new_location = int(index[1])

        # Add package to optimized package list
        # Remove package from packages to check
        # Update current_location
        for index in truck_distance_list:  # section 4
            # current_location = 0

            if check_current_distance(current_location, int(index[1])) == closest_dist:
                if truck_number == 1:
                    # replace
                    # first_optimized_truck.append(index)
                    # first_optimized_truck_index_list.append(index[1])
                    # pop_value = truck_distance_list.index(index)
                    # truck_distance_list.pop(pop_value)
                    # current_location = new_location
                    manage_queue(
                        first_optimized_truck, first_optimized_truck_index_list, index,
                    )
                    calculate_shortest_distance(
                        truck_distance_list, 1, current_location
                    )
                elif truck_number == 2:
                    # replace
                    # second_optimized_truck.append(index)
                    # second_optimized_truck_index_list.append(index[1])
                    # pop_value = truck_distance_list.index(index)
                    # truck_distance_list.pop(pop_value)
                    # current_location = new_location
                    manage_queue(
                        second_optimized_truck,
                        second_optimized_truck_index_list,
                        index,
                    )
                    calculate_shortest_distance(
                        truck_distance_list, 2, current_location
                    )
                elif truck_number == 3:
                    # replace
                    # third_optimized_truck.append(index)
                    # third_optimized_truck_index_list.append(index[1])
                    # pop_value = truck_distance_list.index(index)
                    # truck_distance_list.pop(pop_value)
                    # current_location = new_location
                    manage_queue(
                        third_optimized_truck, third_optimized_truck_index_list, index,
                    )
                    calculate_shortest_distance(
                        truck_distance_list, 3, current_location
                    )

        # except IndexError:
        #     pass
