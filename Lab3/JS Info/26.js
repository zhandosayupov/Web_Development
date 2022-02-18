let calculator = {
    sum() {
        return this.a + this.b;
    },
    mul() {
        return this.a * this.b;
    },
    read() {
        this.a = Number(prompt('a?', 0));
        this.b = Number(prompt('b?', 0));
    }
};