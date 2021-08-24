function valida(){
    var usuario,contraseña,email,telefono,ciudad;

    usuario=document.getElementById("usuario").value;
    contraseña=document.getElementById("contraseña").value;
    email=document.getElementById("email").value;
    telefono=document.getElementById("telefono").value;
    ciudad=document.getElementById("ciudad").value;

    if(usuario===""  && email==="" && telefono==="" && ciudad==="" ){
        alert("Debe llenar todos los campos");
        
       
       } else if(contraseña===""){
alert("Debes introducir una contraseña");

}

else if(email===""){
alert("Debes introducir un email");

}
else if(ciudad===""){
alert("Debes introducir tu ciudad de origen");

} 
       else{
        alert("Registro exitoso");
        return true;

        
    }
}