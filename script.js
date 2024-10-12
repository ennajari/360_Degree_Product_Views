// Données des produits
const products = [
    { id: 1, name: "Casquette", price: 39.99, image: "data/images/Ball_Cap/image1.png", images: 36, prefix: "data/images/Ball_Cap/image", rating: 4.5 },
    { id: 2, name: "Chaussures", price: 59.99, image: "data/images/Shoses/image1.png", images: 60, prefix: "data/images/Shoses/image", rating: 4.2 },
    { id: 3, name: "T-shirt", price: 24.99, image: "data/images/Triko/image1.png", images: 48, prefix: "data/images/Triko/image", rating: 4.7 },
    { id: 4, name: "Montre", price: 79.99, image: "data/images/Watch/image1.png", images: 60, prefix: "data/images/Watch/image", rating: 4.8 }
];

let cart = [];

class ProductViewer {
    constructor(element) {
        this.element = element;
        this.imageCount = parseInt(element.getAttribute('data-images'));
        this.imagePrefix = element.getAttribute('data-prefix');
        this.currentImageIndex = 1;
        this.isDragging = false;
        this.startX = 0;
        this.sensitivity = 5;
        this.initViewer();
    }

    initViewer() {
        const img = document.createElement('img');
        img.src = `${this.imagePrefix}1.png`;
        img.alt = "Product image";
        img.draggable = false;
        img.oncontextmenu = () => false;
        img.style.pointerEvents = 'none';

        const container = document.createElement('div');
        container.style.position = 'relative';
        container.appendChild(img);

        const overlay = document.createElement('div');
        overlay.style.position = 'absolute';
        overlay.style.top = '0';
        overlay.style.left = '0';
        overlay.style.width = '100%';
        overlay.style.height = '100%';
        container.appendChild(overlay);

        this.element.appendChild(container);
        
        this.element.addEventListener('mousedown', this.onMouseDown.bind(this));
        this.element.addEventListener('mousemove', this.onMouseMove.bind(this));
        this.element.addEventListener('mouseup', this.onMouseUp.bind(this));
        this.element.addEventListener('mouseleave', this.onMouseUp.bind(this));
        this.element.addEventListener('contextmenu', (e) => e.preventDefault());
    }

    onMouseDown(event) {
        this.isDragging = true;
        this.startX = event.clientX;
        this.element.style.cursor = 'grabbing';
    }

    onMouseMove(event) {
        if (!this.isDragging) return;
    
        const deltaX = event.clientX - this.startX;
        if (Math.abs(deltaX) >= this.sensitivity) {
            const direction = deltaX > 0 ? 1 : -1; // Suivre le sens du curseur
            this.rotateImage(direction);
            this.startX = event.clientX;
        }
    }

    onMouseUp() {
        this.isDragging = false;
        this.element.style.cursor = 'grab';
    }

    rotateImage(direction) {
        this.currentImageIndex = (this.currentImageIndex + direction - 1 + this.imageCount) % this.imageCount + 1;
        const img = this.element.querySelector('img');
        img.src = `${this.imagePrefix}${this.currentImageIndex}.png`;
    }
}

function displayProducts() {
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';

    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'bg-white shadow-md rounded-lg overflow-hidden';
        productElement.innerHTML = `
            <div class="product-viewer" data-images="${product.images}" data-prefix="${product.prefix}"></div>
            <div class="p-4">
                <h3 class="text-lg font-medium mb-2">${product.name}</h3>
                <div class="star-rating mb-2">${generateStarRating(product.rating)}</div>
                <p class="text-gray-600 mb-4">${product.price.toFixed(2)} €</p>
                <div class="quantity-control mb-4">
                    <button class="quantity-btn minus">-</button>
                    <input type="number" class="quantity-input" value="1" min="1" max="10">
                    <button class="quantity-btn plus">+</button>
                </div>
                <button class="add-to-cart-btn bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded w-full mb-2" data-id="${product.id}">
                    Ajouter au panier
                </button>
                <button class="zoom-btn bg-green-500 hover:bg-green-600 text-white font-medium py-2 px-4 rounded w-full" data-image="${product.image}">
                    Zoom
                </button>
            </div>
        `;
        productList.appendChild(productElement);

        new ProductViewer(productElement.querySelector('.product-viewer'));
        
        const quantityInput = productElement.querySelector('.quantity-input');
        const minusBtn = productElement.querySelector('.minus');
        const plusBtn = productElement.querySelector('.plus');
        
        minusBtn.addEventListener('click', () => updateQuantity(quantityInput, -1));
        plusBtn.addEventListener('click', () => updateQuantity(quantityInput, 1));
        
        const addToCartBtn = productElement.querySelector('.add-to-cart-btn');
        addToCartBtn.addEventListener('click', () => addToCart(product, parseInt(quantityInput.value)));

        const zoomBtn = productElement.querySelector('.zoom-btn');
        zoomBtn.addEventListener('click', () => showZoomedImage(product.image));
    });
}

function generateStarRating(rating) {
    const fullStars = Math.floor(rating);
    const halfStar = rating % 1 >= 0.5;
    const emptyStars = 5 - fullStars - (halfStar ? 1 : 0);

    return '★'.repeat(fullStars) + (halfStar ? '½' : '') + '☆'.repeat(emptyStars);
}

function updateQuantity(input, delta) {
    let value = parseInt(input.value) + delta;
    value = Math.max(1, Math.min(value, 10));
    input.value = value;
}

function addToCart(product, quantity) {
    const existingItem = cart.find(item => item.id === product.id);
    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        cart.push({ ...product, quantity });
    }
    updateCartCount();
    animateCartIcon();
}

function updateCartCount() {
    const cartCount = document.getElementById('cart-count');
    const totalItems = cart.reduce((total, item) => total + item.quantity, 0);
    cartCount.textContent = totalItems;
}

function animateCartIcon() {
    const cartIcon = document.getElementById('cart-icon');
    cartIcon.classList.add('shake');
    setTimeout(() => cartIcon.classList.remove('shake'), 500);
}

function showCart() {
    const cartModal = document.getElementById('cart-modal');
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    
    cartItems.innerHTML = '';
    let total = 0;
    
    cart.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.className = 'flex justify-between items-center mb-2';
        itemElement.innerHTML = `
            <span>${item.name} x${item.quantity}</span>
            <span>${(item.price * item.quantity).toFixed(2)} €</span>
        `;
        cartItems.appendChild(itemElement);
        total += item.price * item.quantity;
    });
    
    cartTotal.textContent = `${total.toFixed(2)} €`;
    cartModal.classList.remove('hidden');
    document.body.classList.add('modal-open');
}

function closeCart() {
    const cartModal = document.getElementById('cart-modal');
    cartModal.classList.add('hidden');
    document.body.classList.remove('modal-open');
}

function checkout() {
    alert('Merci pour votre commande !');
    cart = [];
    updateCartCount();
    closeCart();
}

function showZoomedImage(imageSrc) {
    const zoomModal = document.getElementById('zoom-modal');
    const zoomedImage = document.getElementById('zoomed-image');
    
    zoomedImage.src = imageSrc;
    zoomModal.classList.remove('hidden');
    document.body.classList.add('modal-open');
}

function closeZoomedImage() {
    const zoomModal = document.getElementById('zoom-modal');
    zoomModal.classList.add('hidden');
    document.body.classList.remove('modal-open');
}

document.addEventListener('DOMContentLoaded', () => {
    displayProducts();
    
    const cartIcon = document.getElementById('cart-icon');
    cartIcon.addEventListener('click', showCart);
    
    const closeCartBtn = document.getElementById('close-cart');
    closeCartBtn.addEventListener('click', closeCart);
    
    const checkoutBtn = document.getElementById('checkout');
    checkoutBtn.addEventListener('click', checkout);

    const closeZoomBtn = document.getElementById('close-zoom');
    closeZoomBtn.addEventListener('click', closeZoomedImage);
});