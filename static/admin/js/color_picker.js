document.addEventListener('DOMContentLoaded', function() {
    const colorPickers = document.querySelectorAll('input[type="color"]');
    
    colorPickers.forEach(picker => {
        // Fanya kioo kiwe kidogo, kizuri, na kiwe na nafasi ya kuandika namba pembeni
        picker.style.width = '80px';
        picker.style.height = '40px';
        picker.style.cursor = 'pointer';
        picker.style.borderRadius = '6px';
        picker.style.border = '1px solid #ccc';
        picker.style.padding = '2px';
        picker.style.marginTop = '5px';
        
        // Badilisha muonekano wa sanduku (wrapper)
        const wrapper = picker.parentElement;
        wrapper.style.display = 'flex';
        wrapper.style.alignItems = 'center';
        wrapper.style.gap = '10px';
        
        // Ongeza sanduku la kuandika namba (Hex code) pembeni ya kioo cha rangi
        const textInput = document.createElement('input');
        textInput.type = 'text';
        textInput.value = picker.value;
        textInput.style.width = '100px';
        textInput.style.padding = '8px';
        textInput.style.border = '1px solid #ccc';
        textInput.style.borderRadius = '4px';
        
        wrapper.appendChild(textInput);
        
        // Wakati rangi inabadilishwa kwenye kioo, namba zibadilike
        picker.addEventListener('input', function() {
            textInput.value = this.value;
        });
        
        // Wakati namba zinabadilishwa, kioo kibadilike
        textInput.addEventListener('input', function() {
            if(this.value.startsWith('#') && (this.value.length === 4 || this.value.length === 7)) {
                picker.value = this.value;
            }
        });
    });
});