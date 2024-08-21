import { HtmlHTMLAttributes } from "react";
import { Link } from "react-router-dom";

type ClickImageProps = HtmlHTMLAttributes<HTMLImageElement> & {
  href: string;
  src: string;
  alt: string;
};

export function ClickImage({ src, href, alt, ...props }: ClickImageProps) {
  return (
    <Link to={href}>
      <img src={src} alt={alt} {...props} />
    </Link>
  );
}
