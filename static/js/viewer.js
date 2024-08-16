document.addEventListener('DOMContentLoaded', function() {
    const viewer = document.getElementById('viewer');
    const images = viewer.getElementsByClassName('viewer-image');
    let currentIndex = 0;
    let startX;
    let isDragging = false;

    function showImage(index) {
        for (let i = 0; i < images.length; i++) {
            images[i].style.display = i === index ? 'block' : 'none';
        }
    }

    function rotateImage(delta) {
        currentIndex = (currentIndex + delta + images.length) % images.length;
        showImage(currentIndex);
    }

    viewer.addEventListener('mousedown', startDrag);
    viewer.addEventListener('touchstart', startDrag);

    document.addEventListener('mousemove', drag);
    document.addEventListener('touchmove', drag);

    document.addEventListener('mouseup', endDrag);
    document.addEventListener('touchend', endDrag);

    function startDrag(e) {
        isDragging = true;
        startX = e.pageX || e.touches[0].pageX;
        e.preventDefault();
    }

    function drag(e) {
        if (!isDragging) return;
        
        const currentX = e.pageX || e.touches[0].pageX;
        const diff = currentX - startX;
        const sensitivity = 5;

        if (Math.abs(diff) > sensitivity) {
            rotateImage(diff > 0 ? -1 : 1);
            startX = currentX;
        }
    }

    function endDrag() {
        isDragging = false;
    }

    showImage(currentIndex);
});
