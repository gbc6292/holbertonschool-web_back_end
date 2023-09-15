// Implementing class named Currency

class Currency {
    constructor(code, name) {
        if (typeof code === 'string') {
            this._code = code;
        } else {
            throw new TypeError('Code must be a string')
        }

        if (typeof name === 'string') {
            this._name = name;
        } else {
            throw new TypeError('Name must be a string');
        }
    }

    //Getter for code
    get code() {
        return this._code;
    }

    //Setter for code
    set code(newCode) {
        if (typeof newCode === 'string') {
            this._code = newCode;
        } else {
            throw new TypeError('Code must be a string');
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

    displayFullCurrency() {
        return '${ this._name } (${ this._code })';
    }
}

export default Currency