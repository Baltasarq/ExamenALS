# charset: utf-8
# Main


import exam_manager


if __name__ == "__main__":
    # Retrieve user data
    usr_data = exam_manager.create_or_load_data()

    print(exam_manager.build_header(), end="")
    print(usr_data)
    print("\n")

    # Dump data files
    desktop_path = exam_manager.retrieve_desktop_dir()

    exam_manager.create_marks_file(usr_data, exam_manager.MarksFile)
    exam_manager.create_info_file(usr_data, exam_manager.InfoFile)
    exam_manager.pak_zip(usr_data, desktop_path)
    print("Examen comprimido en: " + str(desktop_path) + "...\n")

    # Student's exercises
    import ejercicio1
    ejercicio1.main()

    import ejercicio2
    ejercicio2.main()

    import ejercicio3
    ejercicio3.main()

    import ejercicio4
    ejercicio4.main()

    import ejercicio5
    ejercicio5.main()

    print("Examen comprimido en: " + str(desktop_path) + "...\n")
