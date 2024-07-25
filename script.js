// This is the data for the products array in the store
const products = [
  {
      name: "Cherrys",
      price: 8.00,
      quantity: 0,
      productId: 111,
      image: "images/cherry.jpg",
  },
  {
      name: "Strawberries",
      price: 5.00,
      quantity: 0,
      productId: 222,
      image: "images/strawberry.jpg",
  },
  {
      name: "Oranges",
      price: 4.00,
      quantity: 0,
      productId: 333,
      image: "images/orange.jpg",
  },
];

// The empty cart array
let cart = [];

// Helper function for getting the product by productId from the list of products
function getProductByIdFromList(productId, productList) {
  return productList.find((product) => product.productId === productId);
}

// Helper function to find product index in cart
function getProductIndexInCart(productId) {
  return cart.findIndex(item => item.productId === productId);
}

// addProductToCart function
function addProductToCart(productId) {
  let product = getProductByIdFromList(productId, products);

  if (product) {
    let cartItemIndex = getProductIndexInCart(productId);
    
    if (cartItemIndex === -1) {
      let newCartItem = {...product, quantity: 1};
      cart.push(newCartItem);
    } else {
      cart[cartItemIndex].quantity++;
    }

    product.quantity++;
  }
}

// increaseQuantity function
function increaseQuantity(productId) {
  let cartItemIndex = getProductIndexInCart(productId);
  if (cartItemIndex !== -1) {
    cart[cartItemIndex].quantity++;
  }

  let product = getProductByIdFromList(productId, products);
  if (product) {
    product.quantity++;
  }
}

// decreaseQuantity function
function decreaseQuantity(productId) {
  let productIndex = getProductIndexInCart(productId);
  if (productIndex !== -1) {
    cart[productIndex].quantity--;
    if (cart[productIndex].quantity === 0) {
      // Remove the item from the cart
      cart.splice(productIndex, 1);
    }
  }

  let productInStore = getProductByIdFromList(productId, products);
  if (productInStore && productInStore.quantity > 0) {
    productInStore.quantity--;
  }
}

// removeProductFromCart function
function removeProductFromCart(productId) {
  // Find the product in the cart array
  const productIndexInCart = getProductIndexInCart(productId);

  if (productIndexInCart !== -1) {
    // Remove the product from the cart array
    cart.splice(productIndexInCart, 1);
  }

  // Find the product in the products array and reset its quantity
  let productInStore = getProductByIdFromList(productId, products);
  if (productInStore) {
    productInStore.quantity = 0;
  }
}

// cartTotal function
function cartTotal() {
  return Number(cart.reduce((total, item) => {
      return total + (item.price * item.quantity);
  }, 0));
}

// emptyCart function
function emptyCart() {
    cart = [];
}

// pay function
let totalPaid = 0;
function pay(amountPaid) {
  let total = cartTotal();
  totalPaid += amountPaid;
  let remainingBalance = total - totalPaid;
  if (remainingBalance <= 0) {
    let change = Math.abs(remainingBalance);
    totalPaid = 0;
    emptyCart();
    return Number(change);
  }
  return -Number(remainingBalance);
}

// npm test command to run tests
module.exports = {
   products,
   cart,
   addProductToCart,
   increaseQuantity,
   decreaseQuantity,
   removeProductFromCart,
   cartTotal,
   pay, 
   emptyCart,
}
