import { Link } from "react-router-dom";

type ClickImageProps = {
  src: string;
  href: string;
  alt: string;
};

export function ClickImage({ src, href, alt }: ClickImageProps) {
  return (
    <Link to={href}>
      <img src={src} alt={alt} className="h-48" />
    </Link>
  );
}
