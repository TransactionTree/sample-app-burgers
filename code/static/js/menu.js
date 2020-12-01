function updateCart(cost, itemName) {
  var cart = grabCart();

  if (cart == null || cart.length == 0) {
    sessionStorage.setItem(
      "Cart",
      JSON.stringify([
        {
          item: "0",
          price: 0,
          qty: 0,
        },
      ])
    );
  }

  if (cart[0].item == "0") {
    cart[0].item = itemName;
    cart[0].price = cost;
    cart[0].qty = 1;
    sessionStorage.setItem("Cart", JSON.stringify(cart));
  } else {
    var size = cart.length;
    //TODO Update this method. Last week we rewrote the logic to include the session variable. We are having using pushing changes to this session variable
    for (let i = 0; i < size; i++) {
      //console.log("i = "+ i +", cart.[i].name = " + cart[i].item + " ,itemName: " + itemName);

      if (cart[i].item == itemName) {
        cart[i].qty = cart[i].qty + 1;
        console.log("reached if ---> " + cart[i].item);
        break;
      } else if (i == size - 1) {
        var newItems = {
          item: itemName,
          price: cost,
          qty: 1,
        };
        cart.push(newItems);
      }
    }
    sessionStorage.setItem("Cart", JSON.stringify(cart));
  }
  displayCart();
}

function grabCart() {
  var cart = sessionStorage.getItem("Cart");
  return JSON.parse(cart);
}

function displayCart() {
  var lst = document.getElementById("order_list");
  var cart = grabCart();

  if (cart == null || cart.length == 0) {
    sessionStorage.setItem(
      "Cart",
      JSON.stringify([
        {
          item: "0",
          price: 0,
          qty: 0,
        },
      ])
    );
  }

  if (cart[0].item == "0") {
  } else {
    var tHolder = document.getElementById("total");
    var total = 0.0;
    lst.innerHTML = "";
    for (let i = 0; i < cart.length; i++) {
      var li = document.createElement("li");
      li.appendChild(
        document.createTextNode(cart[i].item + ": " + cart[i].qty)
      );
      lst.appendChild(li);
      total = total + cart[i].price * cart[i].qty;
      tHolder.innerHTML = total;
    }
  }
}

window.onpageshow = function (event) {
  if (event.persisted) {
    window.location.reload();
  }
};
