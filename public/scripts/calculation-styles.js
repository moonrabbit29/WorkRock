const fuzzificationResult = $("#fuzzificationResultContainer")[0]
const rulesUsed = $("#rulesUsed")[0]

window.addEventListener('load',async ()=>{
   fuzzificationResult.hidden = true
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
        console.log(roomTempHTML)
        roomTempHTML.innerHTML = roomTempView(roomTempMember)
        outsideTempHTML.innerHTML = outsideTempView(outsideTempMember)
        peopleHTML.innerHTML = peopleMemberView(peopleMember)

         fuzzificationResult.hidden = false
        
      },
      type: "GET",
    });
})
const rulesView = (rules,) => {

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
               <h2 class="font-weight-bold">${data.few}</h2>
               <p>Sedikit</p>
             </div>
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.moderate}</h2>
               <p class="font-weight-bold">Sedang</p>
             </div>
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.manyMember}</h2>
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
             <h2 class="font-weight-bold">${data.cold}</h2>
             <p>Dingin</p>
           </div>
           <div class="text-light text-center">
             <h2 class="font-weight-bold">${data.mild}</h2>
             <p class="font-weight-bold">Sejuk</p>
           </div>
           <div class="text-light text-center">
             <h2 class="font-weight-bold">${data.normal}</h2>
             <p class="font-weight-bold">Normal</p>
           </div>
           <div class="text-light text-center">
             <h2 class="font-weight-bold">${data.warm}</h2>
             <p class="font-weight-bold">Hangat</p>
           </div>
           <div class="text-light text-center">
             <h2 class="font-weight-bold">${data.hot}</h2>
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
               <h2 class="font-weight-bold">${data.mild}</h2>
               <p>Sejuk</p>
             </div>
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.normal}</h2>
               <p class="font-weight-bold">Normal</p>
             </div>
             <div class="text-light text-center">
               <h2 class="font-weight-bold">${data.warm}</h2>
               <p class="font-weight-bold">Hangat</p>
             </div>
           </div>
         </div>
       </div>
     </div>
   </div>
 </div>`
}