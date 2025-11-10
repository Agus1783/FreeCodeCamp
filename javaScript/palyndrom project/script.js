const textInput = document.getElementById("text-input");
const checkBtn = document.getElementById("check-btn");
const result = document.getElementById("result");

checkBtn.addEventListener('click', () => {
  const inputValue = textInput.value;
  const cleanStr = inputValue.toLowerCase().replace(/[^a-zA-Z0-9]/g,"")
  const reverseStr = cleanStr.split('').reverse().join('');
  
  if (inputValue === '') {
    alert('Please input a value');
  } else if (inputValue.length === 1) {
    result.textContent = `${inputValue} is a palindrome`
  } else if (cleanStr === reverseStr) {
    result.textContent = `${inputValue} is a palindrome`
  } else {
    result.textContent = `${inputValue} is not a palindrome`
  }
});