#! /bin/env python3
# encoding: utf-8


import os
import json
import pathlib
import zipfile
import platform
import unicodedata


AppInfo = {
    "name": "exam",
    "version": "v0.4 20211215"
}

DataFile = "usr_exam_data.json"
MarksFile = "notas.txt"
InfoFile = "usr_exam_data.txt"
ZipFileNamePrefix = "zip_exam-"

ExcludedFilesByExtension = [
    ".ini", ".db",                                          # Windows
    ".DS_Store",                                            # Mac
    ".bak", ".old",                                         # Backup
    ".dex", ".apk", ".ap_", ".kt~", ".kts~", "ktm~",        # Android
    ".com", ".so", ".lib", ".tmp", ".obj", ".out",
    ".o", ".a", ".lai", ".la", ".dylib", ".dll", ".asm~",   # Assembler
    ".exe", ".pdb", ".userprefs",
    ".user", ".suo", ".nupkg", ".pidb", ".cs~",             # C#
    ".pch", ".slo", ".lo", ".c~", ".cpp~",                  # C/C++
    ".mod", ".smod",                                        # Fortran
    ".jar", ".class", ".war", ".ear", ".ctxt", ".java~",    # Java
    "ts~", ".js~", ".html~", ".css~",                       # JavaScript
    ".bpi", ".bpl", ".map", ".dres", ".ocx", "pas~",        # Pascal (Delphi)
    ".pyc", "pyw", ".cache", ".env", ".py~"                 # Python
]


def build_header() -> str:
    return AppInfo["name"] + " " + AppInfo["version"] + "\n"


def remove_accents(input_str: str) -> str:
    nkfd_form = unicodedata.normalize('NFKD',
                                      input_str.encode("utf-8", "ignore")
                                      .decode("ascii", "ignore"))
    return "".join([c for c in nkfd_form if not unicodedata.combining(c)])


class UserData:
    def __init__(self,
                 surname: str,
                 name: str,
                 dni_prefix: str,
                 dni: str,
                 dni_letter: str,
                 email: str):
        name = name.strip().lower()
        surname = surname.strip().lower()
        dni = str(dni).strip()
        dni_letter = dni_letter.strip().upper()
        email = email.strip().lower()

        if len(name) < 2:
            raise Exception("nombre demasiado corto")

        if len(surname) < 2:
            raise Exception("apellido demasiado corto")

        if len(email) < 3:
            raise Exception("e.mail demasiado corto")

        if email.count('@') != 1:
            raise Exception("e.mail solo tiene que tener una '@'")

        if len(dni) < 8:
            raise Exception("DNI demasiado corto")

        if len(dni_letter) != 1:
            raise Exception("la letra del DNI debe ser de longitud exacta 1")

        self._name = name.strip().title()
        self._surname = surname.strip().title()
        self._dni = dni_prefix + str(int(dni)) + dni_letter
        self._email = email

    @property
    def name(self) -> str:
        return self._name

    @property
    def surname(self) -> str:
        return self._surname

    @property
    def email(self) -> str:
        return self._email

    @property
    def dni_prefix(self) -> str:
        return UserData.decompose_dni(self._dni)[0]

    @property
    def dni(self) -> str:
        return UserData.decompose_dni(self._dni)[1]

    @property
    def dni_letter(self) -> str:
        return UserData.decompose_dni(self._dni)[2]

    @property
    def folder_name(self) -> str:
        return remove_accents(self.surname.lower().replace(' ', '_')
                + "_" + self.name.lower().replace(' ', '_')
                + "-" + self.full_dni())

    def full_dni(self) -> str:
        return self._dni

    def full_name(self) -> str:
        return self.surname + ", " + self.name

    def to_dict(self) -> dict:
        toret = {"dni": self.full_dni(), "name": self.name, "surname": self.surname, "email": self.email}

        return toret

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def decompose_dni(dni: str) -> tuple[str]:
        """Return DNI decomposed in parts
            :return: A tuple with three elements: prefix, dni, letter
        """
        dni_start = 0

        for i, x in enumerate(dni):
            if not x.isalpha():
                dni_start = i
                break

        return tuple([dni[:dni_start], dni[dni_start:-1], dni[-1]])

    @staticmethod
    def from_dict(data):
        dec_dni = UserData.decompose_dni(data["dni"])
        toret = UserData(data["surname"], data["name"],
                         dec_dni[0], dec_dni[1], dec_dni[2],
                         data["email"])
        return toret

    @staticmethod
    def from_json(str_data):
        return UserData.from_dict(json.loads(str_data))

    @staticmethod
    def default():
        return UserData("apellidos", "nombre", "", "12345678", "D", "e@mail")

    def __str__(self) -> str:
        return self.full_name() + "(" + self.full_dni() + "): " + self.email


def ask_for(msg: str, default: str, only_digits:bool=False, max_length:int=128, min_length:int=1) -> str:
    toret = ""
    possibilities = "]"

    if min_length <= 0:
        possibilities = "/-]"

    correct = False
    while not correct:
        toret = input(msg + "[" + str(default) + possibilities + ": ").strip()

        if not toret:
            toret = default

        if (min_length < 0
        and toret == "-"):
            toret = ""

        correct = (min_length <= len(toret) <= max_length)

        if (correct
        and only_digits):
            correct = toret.isdigit()

    return toret


def ask_user_data(user_data: UserData):
    correct = False

    while not correct:
        print()

        dni_prefix = ask_for("Dame la letra prefijo de tu DNI: ",
                      user_data.dni_prefix,
                      min_length=-1,
                      max_length=1).upper()
        dni = ask_for("Dame tu DNI (solo digitos): ",
                      str(user_data.dni),
                      only_digits=True,
                      max_length=10)
        dni_letter = ask_for("Dame la letra de tu DNI: ",
                             user_data.dni_letter,
                             only_digits=False,
                             max_length=1).upper()
        name = ask_for("Dame tu nombre propio: ", user_data.name)
        surname = ask_for("Dame tus apellidos: ", user_data.surname)
        email = ask_for("Dame tu e.mail: ", user_data.email)

        try:
            user_data = UserData(surname, name,
                                 dni_prefix, dni, dni_letter, email)
            print(user_data)

            str_correct = ask_for("Es correcto (s/n): ",
                                  "S",
                                  only_digits=False,
                                  max_length=1).upper()
            correct = (str_correct[0] == 'S')
        except Exception as e:
            print("Error recogiendo datos del usuario: " + e.args[0])
            correct = False

    print()
    return user_data


def create_marks_file(user_data: UserData, file_name: str):
    with open(file_name, "wt") as f:
        f.write("\n===\n")
        f.write(str.format("DNI: {0}\n", user_data.full_dni()))
        f.write(str.format("Nombre: {0}, {1}\n",
                              user_data.surname, user_data.name))
        f.write(str.format("e.Mail: {0}", user_data.email))
        f.write("\n===\n\n")
        for i in range(1, 7):
            f.write(str.format("Ejercicio {0:2d}: \n", i))
        f.write("\n\nNota: \n")


def create_info_file(user_data: UserData, file_name: str):
    with open(file_name, "wt") as f:
        f.write(user_data.full_dni() + "\n")
        f.write(user_data.name + "\n")
        f.write(user_data.surname + "\n")
        f.write(user_data.email + "\n")


def create_data_file(user_data: UserData, file_name: str):
    with open(file_name, "wt") as f:
        f.write(user_data.to_json())
        f.write("\n")


def retrieve_data_file(file_name: str):
    try:
        with open(file_name, "rU") as f:
            return UserData.from_json(str.join("\n", f.readlines()))
    except OSError or IOError:
        return None


def pak_zip(user_data):
    output_path = retrieve_desktop_dir()
    file_name = ZipFileNamePrefix + user_data.full_dni() + ".zip"
    file_name = pathlib.Path(output_path) / file_name
    input_path = "."

    print("Empaquetando examen en archivo zip: " + str(file_name) + "...\n")

    with zipfile.ZipFile(file_name, 'w') as zip_handle:
        input_path = input_path.rstrip("\\/")
        for root, dirs, files in os.walk(input_path):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext not in ExcludedFilesByExtension:
                    file_path = os.path.join(root, file)
                    zip_handle.write(file_path, file_path)


def create_or_load_data():
    if os.path.isfile(DataFile):
        toret = retrieve_data_file(DataFile)
    else:
        toret = ask_user_data(UserData.default())
        create_data_file(toret, DataFile)

    return toret


def retrieve_desktop_dir() -> str:
    if platform.system().strip().lower().startswith("windows"):
        return retrieve_desktop_dir_for_windows()
    else:
        return retrieve_desktop_dir_for_linux()


def retrieve_desktop_dir_for_linux() -> str:
    try:
        toret = subprocess.check_output(["xdg-user-dir", "DESKTOP"]).decode().strip()
    except:
        toret = pathlib.Path.home()

    return toret


def retrieve_desktop_dir_for_windows() -> str:
    return str(pathlib.Path.home() / "Desktop")
