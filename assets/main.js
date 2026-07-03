// Mobile nav toggle
document.addEventListener('click',function(e){
  if(e.target.closest('.menubtn')){
    document.querySelector('.nav').classList.toggle('open');
  }
});
// Smooth-close menu on link tap (mobile)
document.querySelectorAll('.nav a').forEach(function(a){
  a.addEventListener('click',function(){document.querySelector('.nav').classList.remove('open');});
});
