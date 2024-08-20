import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import MyPodPage from "./pages/aula/inicio.tsx";
import { IpodPage } from "./pages/aula/ipod.tsx";
import { HackerNewsPage } from "./pages/hacker-news/inicio.tsx";

const router = createBrowserRouter([
  {
    path: "/my-pod",
    element: <MyPodPage />,
  },
  {
    path: "/my-pod/ipod",
    element: <IpodPage />,
  },
  {
    path: "/",
    element: <HackerNewsPage />,
  },
]);
createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
