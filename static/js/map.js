var map = L.map('map').setView([46.505, 8.09], 4);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '<a href="https://hslu.ch">Created by Timo Feddern @ HSLU Digital Construction</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

Object.keys(companies).forEach(function(companyName) {
    var company = companies[companyName];
    var customIcon = L.icon({
        iconUrl: "https://hslu-dc.github.io/compas_rrc_map/company/" + company.name + "/icon.png",
        iconSize: [40, 40],
        iconAnchor: [20, 40],
        popupAnchor: [-0, -40],
        shadowUrl: company.bg,
        shadowUrl: "https://hslu-dc.github.io/compas_rrc_map/company/" + company.name + "/icon_bg.png",
        shadowSize: [40, 40],
        shadowAnchor: [1, 40]
    });
    var marker = L.marker(company.coordinates, { icon: customIcon }).addTo(map);
    var contactInfo = '';
    for (var key in company.contact) {
        if (company.contact.hasOwnProperty(key)) {
            contactInfo += `${key}: <a href="mailto:${company.contact[key]}">${company.contact[key]}</a><br>`;
        }
    }

    var projectsInfo = '';
    company.projects.forEach(function(project) {
        projectsInfo += `<div style="margin-left: 20px;">
                            <b>${project.name}</b><br>
                            ${project.description}<br>
                            <a href="${project.path}">Project Link</a><br>
                         </div>`;
    });

    var popupContent = `<h3>${company.namenice}</h3><br>
                        <b>About us:</b><br>
                        ${company.description}<br>
                        <a href="${company.path}">More info</a><br>
                        <br>
                        <b>Projects:</b><br>
                        ${projectsInfo}<br>

                        <br>
                        <b>Contact:</b><br>
                        ${contactInfo}`;

    marker.bindPopup(popupContent);
});
