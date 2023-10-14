import os
from utils import logger, format_number, Complexity

from algorithms import sorted_fractional_knapsack, median_of_medians_fractional_knapsack, mean_partition_fractional_knapsack
from execution.instance import Instance
from execution.algorithm import Algorithm, AlgorithmCollection
from execution import Dataset, DatasetGroup, DatasetGroupCollection
from execution.instance import InstanceExecutor

class SearchAlgorithmsInstanceExecutor(InstanceExecutor):
    def __init__(self, algorithm_collection, dataset_group_collection):
        super().__init__(algorithm_collection, dataset_group_collection)

    def execute(self):
        i = 0

        repeat = 1
        quantity_of_instances = len(self.dataset_collection.get_datasets()) * len(self.algorithm_collection.get_algorithms()) * repeat

        for _ in range(repeat):
            for dataset in self.dataset_collection.get_datasets():
                data = dataset.get_data()

                for algorithm in self.algorithm_collection.get_algorithms():
                    instance = Instance(algorithm, dataset)

                    uuid = instance.get_uuid()
                    dataset = instance.get_dataset()

                    W = dataset.get_input_size()
                    instance.set_input(W)
                    
                    dataset_name = dataset.get_name()
                    dataset_size = dataset.get_input_size()
                    dataset_type = dataset.get_dataset_type()
                    algorithm_name = instance.get_algorithm().get_name()
                    complexity_steps = instance.complexity_steps()
                    instance_input = instance.get_input()

                    output = instance.execute()
                    formated_execution_time = format_number(instance.get_execution_time())
                    formated_peak_memory_usage = format_number(instance.peak_memory_usage)

                    logger.info(f"Instance {i + 1} of {quantity_of_instances}")
                    i += 1
                    logger.info(f"Algorithm: {instance.get_algorithm().get_name()}")
                    logger.info(f"Dataset: {instance.get_dataset().get_name()}")
                    logger.info(f"Complexity Steps: {complexity_steps}")
                    logger.info(f"Input: {instance_input}")
                    logger.info(f"Output: {output}")
                    logger.info(f"Execution Time: {formated_execution_time}")
                    logger.info(f"Peak Memory Usage: {formated_peak_memory_usage}")
                    logger.info(f'{"-" * 50}')

                    with open(f'data/output.csv', 'a') as file:
                        file.write(f"{uuid},{algorithm_name},{dataset_name},{dataset_size},{formated_execution_time},{formated_peak_memory_usage},{instance_input},{output},{complexity_steps}\n")

                    del instance
                
                del dataset

if __name__ == "__main__":
    dataset_group_collection_path = os.path.abspath("data")
    dataset_group_folder_names = ["random"]
    
    algorithm_collection = AlgorithmCollection()
    dataset_group_collection = DatasetGroupCollection(dataset_group_collection_path, dataset_group_folder_names)

    algorithm_collection.add_algorithm("Sorted - Fractional Knapsack", sorted_fractional_knapsack, Complexity.o_n_log_n)
    algorithm_collection.add_algorithm("Mean Partition - Fractional Knapsack", mean_partition_fractional_knapsack, Complexity.o_n)
    algorithm_collection.add_algorithm("Partition - Fractional Knapsack", median_of_medians_fractional_knapsack, Complexity.o_n)

    executor = SearchAlgorithmsInstanceExecutor(algorithm_collection, dataset_group_collection)
    executor.execute()
