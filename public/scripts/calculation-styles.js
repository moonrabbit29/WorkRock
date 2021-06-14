const fuzzificationResult = $("#fuzzificationResultContainer")[0]
const rulesUsed = $("#setRules")[0]
const maximumImplicant = $('#maximum-implicant')[0]
const defuzifikasiMamdani = $('#defuzifikasi-mamdani')[0]
let rulesSet;

window.addEventListener('load',async ()=>{
   fuzzificationResult.hidden = true
   $('#ruleContainer')[0].hidden = true
   rulesUsed.hidden = true
   $('#defuzifikasi-mamdani-container')[0].hidden =true
   $.ajax({
      url: "http://localhost:5000/api/get-calculation",
      contentType: "application/json;charset=utf-8",
      dataType   : "json",
      success: function (data) {
        console.log(data)
        let roomTempMember= data.insideTempMember
        let outsideTempMember = data.outsideTempMember
        let peopleMember = data.peopleMember

        const roomTempHTML = $('#roomTempContainer')[0]
        const outsideTempHTML = $('#outsideTempContainer')[0]
        const peopleHTML = $('#peopleMemberContainer')[0]
        roomTempHTML.innerHTML = roomTempView(roomTempMember)
        outsideTempHTML.innerHTML = outsideTempView(outsideTempMember)
        peopleHTML.innerHTML = peopleMemberView(peopleMember)
        rulesView(data.rules,data.detail)
        maximumOutputView(data['maximum-Implicant'])
        defuzifikasiView(data.defuzifikasi)
        fuzzificationResult.hidden = false
        rulesUsed.hidden = false
        $('#defuzifikasi-mamdani-container')[0].hidden=false
        $('#ruleContainer')[0].hidden = false
        
      },
      type: "GET",
    });
})

const defuzifikasiView = (defuzifikasi)=>{
  const numerator = defuzifikasi.numerator.data.replace(/\+ $/,"")
  const denominator = defuzifikasi.denominator.data.replace(/\+ $/,"")
  defuzifikasiMamdani.innerHTML += `<div class="mid mr-3 text-center text-light" style="margin-left:10px; margin-left:10px">
                                        ${numerator}
                                    <hr class="text-light">
                                      ${denominator} 
                                      </div>
                                      <div class="text-light text-center" style="margin-left:10px; margin-left:10px">
                                          =
                                      </div>
                                      <div class="right text-center text-light">
                                          ${defuzifikasi.numerator.value}
                                          <hr class="elegant-color text-light">
                                          ${defuzifikasi.denominator.value}
                                      </div>
                                      <div class="left text-light" style="margin-left:10px; margin-left:10px">  = ${defuzifikasi.numerator.otuputValue} </div>  
                                        `
}

const maximumOutputView = (fuzzyOutput)=>{
  console.log(fuzzyOutput)
  const dingin = (e)=>{
    let stringConstruct=''
    for(let i=0;i<e.length-1;i++){
        stringConstruct+=` µDingin[${e[i]}] V`
    }
    stringConstruct = stringConstruct.slice(0,-1)
    if (e.length==1){
      return `µDingin[${e[0]}]`
    }
    else{
      return (e.length==0) ?' µDingin[0]' : stringConstruct
    }
    
  }
  const cukup_dingin = (e)=>{
    let stringConstruct=''
    for(let i=0;i<e.length-1;i++){
        stringConstruct+=` µCukupDingin[${e[i]}] V`
    }
    stringConstruct = stringConstruct.slice(0,-1)
    if (e.length==1){
      return `µCukupDingin[${e[0]}]`
    }
    else{
      return (e.length==0) ?' µCukupDingin[0]' : stringConstruct
    }
  }
  const sejuk = (e)=>{
    let stringConstruct=''
    for(let i=0;i<e.length-1;i++){
        stringConstruct+=` µSejuk[${e[i]}] V`
    }
    stringConstruct = stringConstruct.slice(0,-1)
    if (e.length==1){
      return `µSejuk[${e[0]}]`
    }
    else{
      return (e.length==0) ?' µSejuk[0]' : stringConstruct
    }
  }
  const normal= (e)=>{
    let stringConstruct=''
    for(let i=0;i<e.length-1;i++){
        stringConstruct+=`µNormal[${e[i]}] V`
    }
    stringConstruct = stringConstruct.slice(0,-1)
    if (e.length==1){
      return `µNormal[${e[0]}]`
    }
    else{
      return (e.length==0) ?' µNormal[0]' : stringConstruct
    }
  }

  maximumImplicant.innerHTML += "<p>µDingin = "+ dingin(fuzzyOutput.cold) + "</P> <br>"
  maximumImplicant.innerHTML += "<p>µCukupDingin = " + cukup_dingin(fuzzyOutput.quitecold) + "</p><br>"
  maximumImplicant.innerHTML += "<p>µSejuk = " + sejuk(fuzzyOutput.mild) + "</p><br>"
  maximumImplicant.innerHTML += "<p>µNormal = "+ normal(fuzzyOutput.normal)+"</p><br>"

}

const countDecimals = function (value) { 
  if ((value % 1) != 0) 
      return value.toString().split(".")[1].length;  
  return 0;
};

function getRulesJSON(){
  return $.getJSON('static/data/rules.json',(data)=>{
    rulesSet =data
  })
}
const rulesView = async (rules,detail) => {
  try{
    await getRulesJSON()
    rules.forEach((el,index) => {
          const detailedRule = rulesSet[el].description.split(';')
          rulesUsed.innerHTML += `<p>${el}. ${rulesSet[el].rules}</p>
                                  <br>
                                  <p>Detail : <br>
                                  <p>${detailedRule[0]}(${detail[index][0]})</p>
                                  <p>${detailedRule[1]}(${detail[index][1]})</p>
                                  <p>${detailedRule[2]}(${detail[index][2]})</p>
                                  <p> Otuput ${detailedRule[3]}(${detail[index][3]}) </p>
                                  <br>
                                  `
    });
  }catch(err){
    console.log(err)
  }
 
}
const peopleMemberView = (data) => {
   return `     <div class="row">
   <div class="col-12">
     <div class="col-12 d-flex justify-content-center">
       <h3 class="tex-center text-primary font-weight-bold">
         Orang dalam ruangan
       </h3>
     </div>
   </div>
   <div class="col-12 mt-3">
     <div class="card bg-dark">
       <div class="card-body">
         <div id="fuzzyResult ">
           <div class="d-flex justify-content-around">
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.few.toFixed(countDecimals(data.few)>=3?3:2)}</h2>
               <p>Sedikit</p>
             </div>
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.moderate.toFixed(countDecimals(data.moderate)>=3?3:2)}</h2>
               <p class="font-weight-bold">Sedang</p>
             </div>
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.manyMember.toFixed(countDecimals(data.manyMember)>=3?3:2)}</h2>
               <p class="font-weight-bold">Banyak</p>
             </div>
           </div>
         </div>
       </div>
     </div>
   </div>
 </div>`
}

const roomTempView = (data)=>{
   return ` <div class="col-12 d-flex justify-content-center">
   <h3 class="tex-center text-primary font-weight-bold">Suhu ruangan</h3>
 </div>
 <div class="col-12 mt-3">
   <div class="card bg-dark">
     <div class="card-body">
       <div id="fuzzyResult ">
         <div class="d-flex justify-content-around">
           <div class="text-light text-center">
             <h2 class="font-weight-bold">${data.cold.toFixed(countDecimals(data.cold)>=3?3:2)}</h2>
             <p>Dingin</p>
           </div>
           <div class="text-light text-center">
             <h2 class="font-weight-bold">${data.mild.toFixed(countDecimals(data.mild)>=3?3:2)}</h2>
             <p class="font-weight-bold">Sejuk</p>
           </div>
           <div class="text-light text-center">
             <h2 class="font-weight-bold">${data.normal.toFixed(countDecimals(data.normal)>=3?3:2)}</h2>
             <p class="font-weight-bold">Normal</p>
           </div>
           <div class="text-light text-center">
             <h2 class="font-weight-bold">${data.warm.toFixed(countDecimals(data.warm)>=3?3:2)}</h2>
             <p class="font-weight-bold">Hangat</p>
           </div>
           <div class="text-light text-center">
             <h2 class="font-weight-bold">${data.hot.toFixed(countDecimals(data.hot)>=3?3:2)}</h2>
             <p class="font-weight-bold">Panas</p>
           </div>
         </div>
       </div>
     </div>
   </div>
 </div>`
}

const outsideTempView = (data)=>{
   return `   <div class="row">
   <div class="col-12 d-flex justify-content-center">
     <h3 class="tex-center text-primary font-weight-bold">
       Suhu luar ruangan
     </h3>
   </div>
   <div class="col-12 mt-3">
     <div class="card bg-dark">
       <div class="card-body">
         <div id="fuzzyResult ">
           <div class="d-flex justify-content-around">
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.mild.toFixed(countDecimals(data.mild)>=3?3:2)}</h2>
               <p>Sejuk</p>
             </div>
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.normal.toFixed(countDecimals(data.normal)>=3?3:2)}</h2>
               <p class="font-weight-bold">Normal</p>
             </div>
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.warm.toFixed(countDecimals(data.warm)>=3?3:2)}</h2>
               <p class="font-weight-bold">Hangat</p>
             </div>
           </div>
         </div>
       </div>
     </div>
   </div>
 </div>`
}