// Implementing a class named HolbertonCourse

class HolbertonCourse {
    constructor(name, length, students) {
        // Verifying the types of attributes during objects creation
        if (typeof name == 'string') {
            this._name = name;
        } else {
            throw new TypeError('Name must be a string');
        }

        if (typeof length == 'number') {
            this._length = length;
        } else {
            throw new TypeError('Lenght must be a number');
        }

        if (Array.isArray(students) && students.every((student) => typeof student === 'string')) {
            this._students = students;
        } else {
            throw new TypeError('Student must be an array of strings');
        }
    }

    //Getter for name
    get name() {
        return this._name;
    }

    //Setter for name
    set name(newName) {
        if (typeof newName === 'string') {
            this._name = newName;
        } else {
            throw new TypeError('Name must be a string');
        }
    }

    //Getter for length
    get length() {
        return this._length;
    }

    //Setter for length
    set length(newLength) {
        if (typeof newLength === 'number') {
            this._length = newLength;
        } else {
            throw new TypeError('Length must be a number');
        }
    }

    //Getter for students
    get student() {
        return this._students;
    }

    //Setter for students
    set students(newStudents) {
        if (Array.isArray(newStudents) && newStudents.every((student) => typeof student === 'string')) {
            this._students = newStudents;
        } else {
            throw new TypeError('Student must be an array of strings');
        }
    }
}

export default HolbertonCourse;