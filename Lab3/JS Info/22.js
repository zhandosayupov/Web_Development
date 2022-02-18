function checkAge(age) {
    if(age > 18) {
        return true;
    }
    return confirm('Did parents allow you?');
}

function min(a,b) {
    if (a < b) {
        return a;
    }
    return b;
}

function pow(x,n) {
    let result = 1;
    for (let i = 0; i < n; i++) {
        result *= x;
    }
    return result;
}

function ask(question, yes, no) {
    if (confirm(question)) yes();
    else no();
}

ask(
    "Do you agree?",
    () => alert("You agreed."),
    () => alert("You canceled the execution.")
);
