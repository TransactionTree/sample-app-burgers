function onClickSidebarItem(itemId, sectionId) {
    // Static class names of elements in 'About' page
    var aboutSection = 'about-section';
    var aboutSectionHidden = 'about-section-hidden';
    var sidebarItemCurrent = 'sidebar-item-current';

    // Hide content from all visible sections in 'About' page
    var sections = document.querySelectorAll('.' + aboutSection);
    if (sections) {
        sections.forEach(function(section) {
            // Do not add hidden class to any section more than once
            if (!section.classList.contains(aboutSectionHidden)) {
                section.classList.add(aboutSectionHidden);
            }
        });
    }

    // Remove highlight from previous section within sidebar
    var highlightedItem = document.querySelector('.' + sidebarItemCurrent);
    if (highlightedItem) {
        highlightedItem.classList.remove(sidebarItemCurrent);
    }

    // Only show the content from the selected section
    var selectedSection = document.querySelector('#' + sectionId);
    if (selectedSection) {
        selectedSection.classList.remove(aboutSectionHidden);
    }

    // Add highlight to current section within sidebar
    var selectedItem = document.querySelector('#' + itemId);
    if (selectedItem && !selectedItem.classList.contains(sidebarItemCurrent)) {
        selectedItem.classList.add(sidebarItemCurrent);
    }
}

function onClickNavButton(itemId, sectionId) {
    // Update the content displayed in the 'About' page
    onClickSidebarItem(itemId, sectionId);

    // Scroll back to top of the page when content loads
    window.scrollTo(0, 0);
}