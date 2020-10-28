

if (sessionStorage.getItem("Cart") === null){
    sessionStorage.setItem('Cart', JSON.stringify([{
                                        item: '0',
                                        price: 0,
                                        qty: 0,
                                   }]));
}
console.log(sessionStorage.getItem('Cart'));
