import uuid
import time
import random
from utils.logger import logger
from utils import get_data_from_file, Folder
from algorithms import Item

class Dataset:
    def __init__(self, file):
        self.set_file(file)

    def set_file(self, file):
        self.file = file

        dataset_type = self.file.folder.get_name()
        self.set_dataset_type(dataset_type)

    def set_dataset_type(self, dataset_type):
        self.dataset_type = dataset_type

    def get_file(self):
        return self.file

    def get_name(self):
        file_name = self.file.get_name()
        name = file_name.replace(".txt", "")
        return name

    def get_path(self):
        file = self.get_file()
        folder_path = file.get_path()
        file_name = file.get_name()
        path = f"{folder_path}/{file_name}"
        return path

    def get_data(self):
        # file = self.get_file()
        # file_path = file.get_path()
        # file_name = file.get_name()
        
        if hasattr(self, "data"):
            return self.data

        data = []
        w = []
        v = []
        size = self.get_input_size()

        for i in range(size):
            peso = random.randint(1, size)
            valor = random.randint(1, size)
            w.append(peso)
            v.append(valor)

        random.shuffle(v)
        random.shuffle(w)

        for i in range(size):
            data.append(Item(w[i], v[i]))

        self.data = data
        return self.data

        # file_full_path = f'{file_path}/{file_name}'
        # self.data = get_data_from_file(file_full_path)
        # return self.data

    def get_input_size(self):
        return int(self.get_name().replace("itens_", ""))

    def get_dataset_type(self):
        return self.dataset_type

class DatasetGroup:
    def __init__(self, folder):
        self.folder = folder

    def get_datasets(self):
        datasets = []
        files = self.folder.get_files_from_directory()
        text_files = list(filter(lambda file: file.get_name().endswith(".txt"), files))
        sorted_text_files = sorted(text_files, key=lambda file: int(file.get_name().replace("itens_", "").replace(".txt", "")))

        for file in sorted_text_files:
            dataset = Dataset(file)
            datasets.append(dataset)

        return datasets


class DatasetGroupCollection:
    def __init__(self, dataset_group_collection_path, dataset_group_folder_names):
        self.set_dataset_group_collection_path(dataset_group_collection_path)
        self.set_dataset_group_folder_names(dataset_group_folder_names)

    def set_dataset_group_collection_path(self, dataset_group_collection_path):
        self.dataset_group_collection_path = dataset_group_collection_path

    def set_dataset_group_folder_names(self, dataset_group_folder_names):
        self.dataset_group_folder_names = dataset_group_folder_names

    def get_dataset_folders(self):
        folders = []
        for dataset_folder_name in self.dataset_group_folder_names:
            folder = Folder(f"{self.dataset_group_collection_path}/{dataset_folder_name}")
            folders.append(folder)

        return folders

    def get_groups(self):
        folders = self.get_dataset_folders()
        groups = []

        for folder in folders:
            group = DatasetGroup(folder)
            groups.append(group)

        return groups

    def get_datasets(self):
        groups = self.get_groups()
        datasets = []

        for group in groups:
            group_datasets = group.get_datasets()
            datasets.extend(group_datasets)

        return datasets
