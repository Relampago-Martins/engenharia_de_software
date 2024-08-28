import { NoticiaPreview } from "@/entities/noticia-card/lib/types";

export const noticias: NoticiaPreview[] = [
    {
      slug: "not-1",
      urlCapa:
        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKmMX999zXB84oRNczWEK4W8VodaujsXWikVA1avU_osbjwleTfC79P6nFmxp3rUPGQk3ZKNCc93KRO_m8cO5yTfCeksQxNdWJl5__OqjppwavG_7bYX0ZgAihKpCd3nJ5SApPf490exk3_j6suXuci9htjITCz2GYWVtZz6GZgsBwIOWMYERIQ_zvB9W7/s728-rw-e365/chinese-hacker.png",
      titulo: "macOS Version of HZ RAT Backdoor Targets Chinese Messaging App Users",
      dataPublicacao: new Date(),
      tag: "Malware",
      resumo:
        "A new macOS version of the HZ RAT has been discovered in the wild, targeting users of the Chinese messaging app QQ. The backdoor is capable of exfiltrating files, capturing screenshots, and executing arbitrary commands on the infected machine.",
    },
    {
      slug: "noticia-2",
      urlCapa:
        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_E4LUK0YF-ig9M9pBoT67TAwZ_EzcZ2sYtFmzhIow9hXpx5A16jE5zkc9aXH0Bd7BdyNYmTDzEs1NnMvog-KgTlDRJw4Tfn1LX-0HBXpixC_qm2Z_0-aInNUMr8BnPDGGltxHtwJ3vMuBkzC3OFDmfEp1MXs1QmUMhui-LaqDgWWfSJqJ1dNGQSgxo1cu/s728-rw-e365/sonic.jpg",
      titulo: "SonicWall Issues Critical Patch for Firewall Vulnerability Allowing Unauthorized Access",
      dataPublicacao: new Date(),
      tag: "Vulnerability",
      resumo:
        "SonicWall has released a critical security patch for a vulnerability affecting its Network Security Appliance (NSA) and Secure Mobile Access (SMA) products. The flaw, tracked as CVE-2021-20016, could allow attackers to gain unauthorized access to the firewall.",
    },
    {
      slug: "noticia-3",
      urlCapa:
        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxsQTTiXQzZa0E3sRFj5kg95PFamXiK_e14EjTGgqYqB0J4YYdDecYS4NUlG6j7D-s6F-WfxIjnImbNssOObVnU3SUNgsBbzWA2lW5sgjl2q1JSP-s61TTlCORLhxKjR1J7-_5g8D_FK-HsxlWrNqNoxlWSK0ps8vzC5kFtitGfgrpWrQdGOWbg0QsOAEv/s728-rw-e365/Uber.png",
      titulo: "Dutch Regulator Fines Uber €290 Million for GDPR Violations in Data Transfers to U.S.",
      dataPublicacao: new Date(),
      tag: "Data Privacy",
      resumo:
        "The Dutch Data Protection Authority (AP) has fined Uber €290 million for violating the General Data Protection Regulation (GDPR) in its data transfers to the U.S. The regulator found that the ride-hailing company failed to protect the personal data of its drivers and passengers.",
    },
  ];