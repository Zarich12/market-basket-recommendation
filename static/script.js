document.getElementById('output').innerHTML = location.search;
$(".chosen-select").chosen();


function printAll() {

var str="",i;

for (i=0;i<myForm.myOption.options.length;i++) {
    if (myForm.myOption.options[i].selected) {
        str = str + i + " ";
    }
}

document.getElementById("myText").value = str;

}
