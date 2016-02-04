from os import listdir

class detect_linux_distro():
    """Detect linux distribution python module"""
    name = []
    id = []
    pretty_name = []
    release_files_in_etc = []

    def __init__(self):
        pass

    def get_distro_name(self , return_all = 0):
        """
        By default function return the first result of which was earned.
        To get all result, set return_all to 1.
        :param return_all: if set to 1, function return a list of all names.
        :return -1: if can't find distribution name.
        :return string: if can find your distribution name.
        :return list: if return_all setted to 1.
        """
        if self.name.__len__() == 0:
            return -1
        if return_all == 0:
            return self.name[0]
        else:
            return self.name

    def get_distro_id(self , return_all = 0):
        """
        By default function return the first result of which was earned.
        To get all result, set return_all to 1.
        :param return_all: if set to 1, function return a list of all ids.
        :return -1: if can't find distribution id.
        :return string: if can find your distribution id.
        :return list: if return_all setted to 1.
        """
        if self.name.__len__() == 0:
            return -1
        if return_all == 0:
            return self.id[0]
        else:
            return self.id

    def get_distro_pretty_name(self , return_all = 0):
        """
        By default function return the first result of which was earned.
        To get all result, set return_all to 1.
        :param return_all: if set to 1, function return a list of all pretty names.
        :return -1: if can't find distribution pretty name.
        :return string: if can find your distribution pretty name.
        :return list: if return_all set to 1.
        """
        if self.name.__len__() == 0:
            return -1
        if return_all == 0:
            return self.pretty_name[0]
        else:
            return self.pretty_name

    def find_release_files_in_etc(self):
        """Find all files which word "release" is in their name in etc folder"""
        etc_file_list = listdir("/etc")
        for f in etc_file_list:
            if 'release' in f:
                self.release_files_in_etc.append(f)

    def detect(self):
        """Try to detect your Linux distribution"""
        self.find_release_files_in_etc()
        for f in self.release_files_in_etc:
            file = open('/etc/' + f , 'r')
            for line in file:
                if line.find('PRETTY_NAME') != -1:
                    pretty_name_nl = line.split('=')[1]
                    self.pretty_name.append( pretty_name_nl[:pretty_name_nl.__len__()-1] )
                elif line.find('NAME') != -1:
                    name_nl = line.split('=')[1]
                    self.name.append( name_nl[:name_nl.__len__()-1] )
                elif line.find('ID') != -1:
                    id_nl = line.split('=')[1]
                    self.id.append( id_nl[:id_nl.__len__()-1] )

    def print_all_result(self):
        """Print all results was earned."""

        print("All distribution name that I found for you: ")
        for name in self.name:
            print(name)

        print()
        print("All ID that I found for you: ")
        for d_id in self.id:
            print(d_id)

        print()
        print("All pretty name that I found for you: ")
        for pretty_name in self.pretty_name:
            print(pretty_name)


d = detect_linux_distro()
d.detect()
print(d.get_distro_name())
print(d.get_distro_id())

# todo: if relase file not found work with => cat /etc/issue | head -n +1 | awk '{print $1}'
