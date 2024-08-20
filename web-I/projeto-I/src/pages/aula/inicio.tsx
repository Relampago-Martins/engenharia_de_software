import appleStore from "../../assets/applestore.jpg";
import britain from "../../assets/britain.jpg";
import myPodLogo from "../../assets/mypod.gif";
import downtown from "../../assets/seattle_downtown.jpg";
import med from "../../assets/seattle_med.jpg";
import shuffle from "../../assets/seattle_shuffle.jpg";
import { ClickImage } from "../../entities/click-imagem";

function MyPodPage() {
  return (
    <div className="bg-gray-100 w-svw h-svh flex flex-col px-8 py-4">
      <div className="flex items-center">
        <img src={myPodLogo} className="object-contain h-20" alt="MyPod logo" />
      </div>
      <div className="py-2">
        <h1 className="text-3xl my-3 font-medium">Welcome to myPod</h1>
        <span>
          myPod Welcome to the place to show off your iPod, wherever you might
          be. Wanna join the fun? All you need is any iPod, from the early
          classic iPod to the latest iPod Nano, the smallest iPod Shuffle to the
          largest iPod Photo, and a digital camera. Just take a snapshot of your
          iPod in your favorite location and we&apos;ll be glad to post it on
          myPod. So, what are you waiting for?
        </span>
      </div>
      <div className="my-4 flex flex-col gap-4">
        <h2 className="text-2xl font-medium">Seattle, Washington</h2>
        <span>
          Me and my iPod in Seattle! You can see rain clouds and the Space
          Needle. You can&apos;t see the 628 coffee shops.
        </span>
        <div className="flex items-center gap-2">
          <ClickImage
            src={med}
            alt="My iPod in Seattle, WA"
            href="/my-pod/ipod"
          />
          <ClickImage
            src={shuffle}
            alt="An iPod Shuffle in Seattle, WA"
            href="/my-pod/ipod"
          />
          <ClickImage
            src={downtown}
            alt="An iPod in downtown Seattle, WA"
            href="/my-pod/ipod"
          />
        </div>
      </div>
      <div className="my-4 flex flex-col gap-4">
        <h2 className="text-2xl font-medium">Birmingham, England</h2>
        <span>
          Here are some iPod photos around Birmingham. We&apos;ve obviously got
          some passionate folks over here who love their iPods. Check out the
          classic red British telephone box!
        </span>
        <div className="flex items-center gap-2">
          <ClickImage
            src={britain}
            alt="An iPod in Birmingham at a telephone box"
            href="/my-pod/ipod"
          />
          <ClickImage
            src={appleStore}
            alt="An iPod at the Birmingham Apple store"
            href="/my-pod/ipod"
          />
        </div>
      </div>
    </div>
  );
}

export default MyPodPage;
