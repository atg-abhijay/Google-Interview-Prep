# Google-Interview-Prep

Coding questions I did in preparation for my Google interviews.

**Note**: There are files that have "2nd Pass" solutions. Those are solutions I wrote the second time around when I solved those problems.

Tree of problems in the repository:
```bash
.
├── Array
│   ├── best_time_buy_sell_stock_121.py
│   ├── container_most_water_11.py
│   ├── contains_duplicate_217.py
│   ├── find_min_rotated_sorted_array_153.py
│   ├── h_index_274.py
│   ├── h_index_ii_275.py
│   ├── maximum_product_subarray_152.py
│   ├── maximum_subarray_53.py
│   ├── product_array_except_self_238.py
│   ├── search_rotated_sorted_array_33.py
│   └── two_sum_1.py
├── Binary
│   ├── counting_bits_338.py
│   ├── missing_number_268.py
│   ├── num_1_bits_191.py
│   ├── reverse_bits_190.py
│   └── sum_two_integers_371.py
├── Dynamic-Programming
│   ├── climbing_stairs_70.py
│   ├── coin_change_322.py
│   ├── combination_sum_39.py
│   ├── combination_sum_III_216.py
│   ├── combination_sum_II_40.py
│   ├── combination_sum_IV_377.py
│   ├── house_robber_198.py
│   ├── house_robber_ii_213.py
│   ├── jump_game_55.py
│   ├── longest_increasing_subsequence_300.py
│   ├── non_overlapping_intervals_435.py
│   └── partition_equal_subset_sum_416.py
├── Geometry
│   ├── check_if_straight_line_1232.py
│   ├── circle_rectangle_overlapping_1401.py
│   ├── k_closest_points_origin_973.py
│   ├── mirror_reflection_858.py
│   ├── queries_points_inside_circle_1828.py
│   └── valid_boomerang_1037.py
├── Graph
│   ├── all_paths_source_target_797.py
│   ├── clone_graph_133.py
│   ├── couples_holding_hands_765.py
│   ├── course_schedule_207.py
│   ├── course_schedule_II_210.py
│   ├── detonate_maximum_bombs_2101.py
│   ├── find_center_star_graph_1791.py
│   ├── find_path_exists_in_graph_1971.py
│   ├── find_town_judge_997.py
│   ├── flower_planting_with_no_adjacent_1042.py
│   ├── is_graph_bipartite_785.py
│   ├── keys_and_rooms_841.py
│   ├── longest_consecutive_sequence_128.py
│   ├── loud_and_rich_851.py
│   ├── maximal_network_rank_1615.py
│   ├── min_vertices_reach_all_nodes_1557.py
│   ├── num_operations_make_network_connected_1319.py
│   ├── num_provinces_547.py
│   ├── num_ways_arrive_at_destination_1976.py
│   ├── number_of_islands_200.py
│   ├── pacific_atlantic_water_flow_417.py
│   ├── possible_bipartition_886.py
│   ├── redundant_connection_684.py
│   └── unique_paths_62.py
├── Hash-Table
│   ├── display_orders_in_restaurant_1418.py
│   ├── duplicates_in_array_442.py
│   ├── num_eq_domino_pairs_1128.py
│   ├── ransom_note_383.py
│   ├── subdomain_visit_count_811.py
│   ├── task_scheduler_621.py
│   └── verifying_alien_dictionary_953.py
├── Heap
│   └── top_k_frequent_elements_347.py
├── Interval
│   ├── insert_interval_57.py
│   ├── interval_list_intersections_986.py
│   └── merge_intervals_56.py
├── Linked-List
│   ├── linked_list_cycle_141.py
│   ├── merge_k_sorted_lists_23.py
│   ├── merge_two_sorted_lists_21.py
│   ├── remove_nth_node_from_end_19.py
│   ├── reorder_list_143.py
│   └── reverse_linked_list_206.py
├── Math
│   └── sqrt_x_69.py
├── Matrix
│   ├── game_of_life_289.py
│   ├── rotate_image_48.py
│   ├── set_matrix_zeroes_73.py
│   ├── spiral_matrix_54.py
│   ├── valid_sudoku_36.py
│   ├── where_will_ball_fall_1706.py
│   └── word_search_79.py
├── Permutation
│   ├── permutations_46.py
│   ├── permutations_II_47.py
│   └── prev_permutation_with_one_swap_1053.py
├── Queue
│   ├── design_circular_deque_641.py
│   ├── dota2_senate_649.py
│   ├── implement_queue_using_stacks_232.py
│   └── product_of_last_k_numbers_1352.py
├── Recursion
│   ├── count_max_bitwise_subsets_2044.py
│   ├── subsets_78.py
│   └── subsets_II_90.py
├── Sorting
│   ├── assign_cookies_455.py
│   ├── pancake_sorting_969.py
│   └── two_city_scheduling_1029.py
├── Stack
│   ├── asteroid_collision_735.py
│   ├── design_browser_history_1472.py
│   ├── exclusive_time_of_functions_636.py
│   ├── min_add_to_make_parentheses_valid_921.py
│   ├── min_remove_to_make_valid_parentheses_1249.py
│   ├── simplify_path_71.py
│   └── valid_parentheses_20.py
├── String
│   ├── group_anagrams_49.py
│   ├── longest_palindromic_substring_5.py
│   ├── palindromic_substrings_647.py
│   ├── valid_anagram_242.py
│   └── valid_palindrome_125.py
├── Tree
│   ├── balanced_binary_tree_110.py
│   ├── binary_tree_level_order_traversal_102.py
│   ├── binary_tree_maximum_path_sum_124.py
│   ├── construct_binary_tree_from_preorder_inorder_105.py
│   ├── invert_binary_tree_226.py
│   ├── kth_smallest_element_bst_230.py
│   ├── lowest_common_ancestor_in_bst_235.py
│   ├── max_depth_binary_tree_104.py
│   ├── same_tree_100.py
│   ├── subtree_of_another_tree_572.py
│   └── validate_binary_search_tree_98.py
├── Trie
│   ├── design_add_search_words_data_structure_211.py
│   ├── implement_trie_prefix_tree_208.py
│   ├── leetcode_212_good_solution.py
│   └── word_search_II_212.py
└── kth_smallest_instructions_1643.py
```